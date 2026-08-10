# Runtime Foundation Templates

Load when creating or materially revising centralized settings, error catalogs, logger construction/injection, correlation context, or throw/catch ownership. Replace every example code, key, path, and surface with project-owned values. These modules are separate owners in a real project; the snippets are grouped here only to show how their contracts connect.

## Central Error Contract And Catalog

Use one stable runtime type plus one strict, sanitized, transport-neutral payload schema. Expand fields only when the project's error contract owns them. This payload is not a public response, event, webhook, or job envelope; the contracts owner declares and maps each external shape.

```ts
import { z } from "zod";

export const errorCodeSchema = z.enum([
  "SYS_UNEXPECTED_ERROR",
  "SYS_CONFIGURATION_INVALID",
  "EXT_PROVIDER_FAILED",
]);

export const appErrorPayloadSchema = z.strictObject({
  _tag: z.literal("AppError"),
  code: errorCodeSchema,
  reason: z.string().min(1),
  message: z.string().min(1),
  severity: z.enum(["info", "warn", "error", "fatal"]),
  retryable: z.boolean(),
  correlationId: z.string().min(1),
});

export type AppErrorCode = z.infer<typeof errorCodeSchema>;
export type AppErrorPayload = z.infer<typeof appErrorPayloadSchema>;
export type AppErrorContext = Readonly<Record<string, unknown>>;

export class AppError extends Error {
  readonly _tag = "AppError" as const;
  readonly code: AppErrorCode;
  readonly reason: string;
  readonly severity: AppErrorPayload["severity"];
  readonly retryable: boolean;
  readonly correlationId: string;
  readonly context: AppErrorContext | undefined;

  constructor(
    input: Omit<AppErrorPayload, "_tag"> & {
      cause?: AppError;
      context?: AppErrorContext;
    },
  ) {
    super(input.message, input.cause === undefined ? undefined : { cause: input.cause });
    this.name = "AppError";
    this.code = input.code;
    this.reason = input.reason;
    this.severity = input.severity;
    this.retryable = input.retryable;
    this.correlationId = input.correlationId;
    this.context = input.context;
  }

  toSerializablePayload(): Readonly<Record<string, unknown>> {
    return {
      _tag: this._tag,
      code: this.code,
      reason: this.reason,
      message: this.message,
      severity: this.severity,
      retryable: this.retryable,
      correlationId: this.correlationId,
    };
  }
}
```

For recursive causes, add both a depth bound and cycle detection. `AppErrorContext` is internal diagnostic state: never place it in the payload schema or copy it through a generic mapper. An external contract may expose only separately declared, bounded, sanitized fields that its boundary schema owns.

Catalog entries own fixed classification; callers supply only operation-specific safe context:

```ts
interface CatalogEntry {
  readonly message: string;
  readonly reason: string;
  readonly retryable: boolean;
  readonly severity: AppErrorPayload["severity"];
}

const ERROR_CATALOG = Object.freeze({
  SYS_UNEXPECTED_ERROR: Object.freeze({
    reason: "unexpected_error",
    message: "An unexpected error occurred",
    severity: "error" as const,
    retryable: false,
  }),
  SYS_CONFIGURATION_INVALID: Object.freeze({
    reason: "configuration_invalid",
    message: "Application configuration is invalid",
    severity: "fatal" as const,
    retryable: false,
  }),
  EXT_PROVIDER_FAILED: Object.freeze({
    reason: "provider_operation_failed",
    message: "The external operation failed",
    severity: "error" as const,
    retryable: true,
  }),
} satisfies Readonly<Record<AppErrorCode, CatalogEntry>>);

type CatalogCode = keyof typeof ERROR_CATALOG;

export function createAppError(input: {
  code: CatalogCode;
  correlationId: string;
  context?: Readonly<Record<string, unknown>>;
  cause?: AppError;
}): AppError {
  return new AppError({
    ...ERROR_CATALOG[input.code],
    code: input.code,
    correlationId: input.correlationId,
    context: input.context,
    cause: input.cause,
  });
}

export function ensureAppError(raw: unknown, correlationId: string): AppError {
  if (raw instanceof AppError) {
    return raw;
  }

  const parsed = appErrorPayloadSchema.safeParse(raw);
  if (parsed.success) {
    return createAppError({
      code: parsed.data.code,
      correlationId,
    });
  }

  return createAppError({
    code: "SYS_UNEXPECTED_ERROR",
    correlationId,
    context: {
      originalType: raw === null ? "null" : typeof raw,
    },
  });
}

export function toAppErrorPayload(
  error: AppError,
  log: {
    error(
      fields: Readonly<Record<string, unknown>>,
      event: string,
    ): void;
  },
): AppErrorPayload {
  try {
    return appErrorPayloadSchema.parse(error.toSerializablePayload());
  } catch (raw) {
    const mappingError = createAppError({
      code: "SYS_UNEXPECTED_ERROR",
      correlationId: error.correlationId,
      context: { operation: "serialize_app_error" },
      cause: ensureAppError(raw, error.correlationId),
    });
    log.error(
      {
        err: mappingError,
        correlationId: error.correlationId,
        operation: "serialize_app_error",
      },
      "app_error_serialization_failed",
    );
    throw mappingError;
  }
}
```

`toSerializablePayload()` produces the errors owner's sanitized, transport-neutral payload; it is not an external wire boundary and must not be passed directly to a response, message, or storage serializer. The errors owner calls `toAppErrorPayload()`, which validates that projection and owns parse failure through catch, normalization, structured logging, and throw. The contracts owner then maps the validated payload into the separately declared external envelope, and the exit adapter applies that mapping.

The payload parser treats the code only as a catalog lookup key. It does not trust inbound reason, message, severity, retryability, or correlation values as classification authority. Internal diagnostic context never enters this payload contract. If an external boundary needs selected diagnostic fields, declare them explicitly in that boundary's schema and copy only a bounded, sanitized allowlist after the catalog helper restores the fixed classification.

In a multi-surface project, expose `createSharedError`, `createApiError`, `createWebError`, and matching `ensure*Error` helpers from their owned subpaths. The semantic rule maps each source surface to its permitted helper.

## Central Settings Loader

The loader is the sole direct environment reader. Its configuration-level lint exception names this file; it contains no inline suppression.

```ts
import { z } from "zod";
import { createAppError } from "../errors/catalog-helpers.js";
import { writeBootstrapDiagnostic } from "../logging/bootstrap-diagnostics.js";

const settingsSchema = z.strictObject({
  NODE_ENV: z.enum(["development", "test", "production"]),
  PORT: z.coerce.number().int().min(1).max(65_535),
  PROVIDER_TIMEOUT_MS: z.coerce.number().int().positive(),
  LOG_LEVEL: z.enum(["debug", "info", "warn", "error"]),
  LOG_DESTINATION: z.enum(["console", "file", "both"]),
});

export type Settings = Readonly<z.infer<typeof settingsSchema>>;

const settingsKeys = [
  "NODE_ENV",
  "PORT",
  "PROVIDER_TIMEOUT_MS",
  "LOG_LEVEL",
  "LOG_DESTINATION",
] as const;

export function loadSettings(): Settings {
  const projected: Record<string, string | undefined> = {};
  for (const key of settingsKeys) {
    projected[key] = process.env[key];
  }

  const parsed = settingsSchema.safeParse(projected);
  if (parsed.success) {
    return Object.freeze(parsed.data);
  }

  const error = createAppError({
    code: "SYS_CONFIGURATION_INVALID",
    correlationId: "bootstrap",
    context: {
      issues: parsed.error.issues.map((issue) => ({
        code: issue.code,
        path: issue.path,
      })),
    },
  });
  writeBootstrapDiagnostic(error);
  throw error;
}
```

For runtime overrides, inspect protected raw key names first. A protected-key attempt creates a fatal catalog error, writes the safe bootstrap diagnostic, and throws. Only after that check may the remaining override object be parsed and merged. Deep-freeze nested settings when they contain arrays/objects.

## Logger Contract And Composition Root

Leaf packages accept the narrow contract they use:

```ts
export interface LogSink {
  debug(fields: Readonly<Record<string, unknown>>, event: string): void;
  error(fields: Readonly<Record<string, unknown>>, event: string): void;
  info(fields: Readonly<Record<string, unknown>>, event: string): void;
  warn(fields: Readonly<Record<string, unknown>>, event: string): void;
}
```

The logging owner builds the Pino logger with UTC timestamps, correlation enrichment, the centralized error serializer, immutable redaction paths, and the configured sink. The composition root creates and injects it. Its typed factory seam lets tests substitute package-owned doubles without changing production callers:

```ts
interface RuntimeFactories {
  readonly createBaseLogger: typeof createBaseLogger;
  readonly createProvider: typeof createProvider;
  readonly createRuntime: typeof createRuntime;
  readonly loadSettings: typeof loadSettings;
}

export function composeRuntime(
  overrides: Partial<RuntimeFactories> = {},
): Runtime {
  const factories: RuntimeFactories = {
    createBaseLogger: overrides.createBaseLogger ?? createBaseLogger,
    createProvider: overrides.createProvider ?? createProvider,
    createRuntime: overrides.createRuntime ?? createRuntime,
    loadSettings: overrides.loadSettings ?? loadSettings,
  };
  let logger: ReturnType<typeof createBaseLogger> | undefined;

  try {
    const settings = factories.loadSettings();
    logger = factories.createBaseLogger({
      level: settings.LOG_LEVEL,
      destination: settings.LOG_DESTINATION,
    });
    const provider = factories.createProvider({
      timeoutMs: settings.PROVIDER_TIMEOUT_MS,
      log: logger.child({ module: "provider" }),
    });
    return factories.createRuntime({
      provider,
      log: logger.child({ module: "runtime" }),
    });
  } catch (raw) {
    const error = ensureAppError(raw, "bootstrap");
    if (logger === undefined) {
      writeBootstrapDiagnostic(error);
    } else {
      logger.error(
        { err: error, correlationId: "bootstrap", operation: "compose_runtime" },
        "runtime_composition_failed",
      );
    }
    throw error;
  }
}
```

The settings schema must declare every field used above. The settings loader logs its local validation failure; the composition catch records the terminal startup disposition. The fallback writer is the logging owner's sole pre-logger channel. Do not access a settings singleton or create a fallback logger inside `createProvider`.

## Catch, Normalize, Log, Then Throw

```ts
export async function fetchRecord(input: {
  correlationId: string;
  id: string;
  log: LogSink;
  signal: AbortSignal;
}): Promise<RecordData> {
  try {
    const response = await providerClient.fetch(input.id, {
      signal: input.signal,
    });
    const parsed = recordResponseSchema.safeParse(await response.json());
    if (!parsed.success) {
      const error = createAppError({
        code: "EXT_PROVIDER_FAILED",
        correlationId: input.correlationId,
        context: { operation: "fetch_record", issueCount: parsed.error.issues.length },
      });
      input.log.error(
        {
          err: error,
          correlationId: input.correlationId,
          operation: "fetch_record",
        },
        "provider_response_invalid",
      );
      throw error;
    }
    return parsed.data;
  } catch (raw) {
    const error = ensureAppError(raw, input.correlationId);
    input.log.error(
      {
        err: error,
        correlationId: input.correlationId,
        operation: "fetch_record",
      },
      "provider_fetch_failed",
    );
    throw error;
  }
}
```

The example intentionally logs twice when the local deliberate throw is caught by the function's terminal catch: one event records the validation decision; the next records terminal disposition. In a real implementation, place the terminal catch at the owner that can decide the final outcome; do not add a catch merely to satisfy syntax.

## Correlation Boundary

At trusted ingress, keep an untrusted external request/delivery ID separate from the generated internal correlation ID, then bind async context around the complete handler. The boundary owns failures from identifier creation, header parsing, context binding, and the awaited handler:

```ts
export async function runRequestBoundary(input: {
  handleRequest: (context: RequestContext) => Promise<Response>;
  log: LogSink;
  request: Request;
}): Promise<Response> {
  let correlationId = "ingress";
  let requestId: string | undefined;
  try {
    correlationId = crypto.randomUUID();
    requestId = readBoundedRequestId(input.request.headers);
    const context: RequestContext =
      requestId === undefined ? { correlationId } : { correlationId, requestId };
    return await withCorrelationContext(
      context,
      () => input.handleRequest(context),
    );
  } catch (raw) {
    const error = ensureAppError(raw, correlationId);
    input.log.error(
      {
        err: error,
        correlationId,
        operation: "run_request_boundary",
        ...(requestId === undefined ? {} : { requestId }),
      },
      "request_boundary_failed",
    );
    throw error;
  }
}
```

The logger mixin reads this context on every event and falls back to `correlationId: "bootstrap"` before a request/job scope exists. The context helper clears storage when the awaited scope completes. The framework's terminal response/error adapter logs its own final disposition when this boundary rethrows.

Failure output: `Blocked: runtime foundation template lacks a project-owned catalog, settings source, logger/correlation path, or catch/log/throw owner.`
