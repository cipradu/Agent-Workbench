---
name: microsoft365
description: Use when reading Outlook mail or Microsoft Teams content through Microsoft 365 MCP tools, including finding or searching email, reading a message body, browsing mail folders, and listing teams, channels, chats, or members, and when such a tool rejects a query parameter or returns 400, 403, or 429.
---

# Microsoft 365 MCP Queries

## When to Use

- Building any call to an `ms-365-mcp-server` tool that lists, searches, or reads mail or Teams data.
- A tool returned `400`, `403`, or `429` and the cause is unclear.
- Choosing between listing, searching, and filtering to answer a question.
- Deciding how to page, how to bound result size, or how to retrieve message body content.

## Do Not Use

- For write operations — send, reply, create, update, delete. Those carry confirmation and permission concerns this skill does not cover.
- For services other than mail and Teams. Calendar, OneDrive, SharePoint, Planner, and To Do have no verified support table here, and guessing is the failure this skill exists to prevent.
- To discover which tools exist. Tool descriptions and `search-tools` already do that.
- To restate a tool's own parameter description. Read that first — it is authoritative for syntax.

## Iron Law

**Every tool advertises the same OData parameters. The endpoint behind it does not accept them all.**

`top`, `skip`, `search`, `filter`, `count`, `orderby`, `select`, and `expand` appear on nearly every list tool because the schema is generated uniformly — not because the endpoint supports them. Passing an unsupported one returns `400`. It is not silently ignored.

Before sending any OData parameter, confirm it in the support table for that endpoint. If the endpoint appears in no table, send the call with **no** OData parameters and shape the result client-side.

## Branch Table

Load exactly one, by what the call touches:

| The call reads | Load |
| --- | --- |
| Mail — messages, folders, attachments, search, message bodies | [Mail queries](references/mail.md) |
| Teams — joined teams, channels, channel messages, chats, chat messages, members | [Teams queries](references/teams.md) |
| Both in one task | Load both, in the order the task needs them |

Do not proceed from memory of a previous session. Load the reference before sending parameters.

## Shared Contract

True for every tool in this server:

- **Parameter names take no `$`.** Pass `search`, `top`, `select`. The server adds the prefix. It also accepts and normalizes `$search`, so either form works.
- **The `search` value carries its own double quotes.** The value must be `"from:sarah"` — quotes included — not `from:sarah`.
- **Message bodies return as plain text by default.** The server sends `Prefer: outlook.body-content-type="text"` on every GET unless `MS365_MCP_BODY_FORMAT=html` is set. Do not plan to strip HTML that will not be there.
- **`fetchAllPages: true`** follows `@odata.nextLink` up to 100 pages and merges the result. Use only when the user explicitly asked for a complete export.
- **`excludeResponse: true`** returns success/failure only, without the payload.
- **Path parameters use their own names**, never `id`: `messageId`, `mailFolderId`, `teamId`, `channelId`, `chatId`.
- **Read-only is a launch flag, not a per-call choice.** If write tools are absent from the tool list, the server was started `--read-only`; no phrasing produces a write.

## Bounding Results

Answer with the smallest result set that satisfies the question.

- Start `top` at 5–15 where the endpoint accepts it. Raise only after a response proves more is needed.
- Pass `select` wherever supported. Unselected message listings return large objects.
- Where an endpoint rejects `top`, **truncate client-side**. A user asking for "the first 5" is describing the answer, not the wire request.

## Rationalizations

| Temptation | Reality | Required action |
| --- | --- | --- |
| "The parameter is in the schema, so the endpoint takes it." | The schema is generated uniformly across all endpoints. | Check the support table. |
| "The user said 'just the first 5', so I must send `top: 5`." | Endpoint support does not bend to user phrasing. | Call without `top`; truncate the answer. |
| "It errored — retry with slightly different parameters." | Blind retry spends throttle budget and repeats the same class of error. | Read the error, find the endpoint in the table, drop every unsupported parameter at once. |
| "`select` worked on the mail endpoint, so it works here." | Support varies per endpoint, even inside one service. | Re-check the table for this exact endpoint. |
| "I'll set `fetchAllPages` so nothing is missed." | It can return a payload far larger than the context window. | Use only on an explicit request for everything. |

## Stop Conditions

Stop and report rather than continuing to call:

- **Two consecutive `400`s on one endpoint.** Retrying will not fix a wrong parameter set. Report the endpoint, the parameters sent, and the error text.
- **`403`.** A permissions or consent problem, not a query problem. Name the scope the operation needs; do not retry with different parameters.
- **`429`.** Honor the `Retry-After` header. Do not retry sooner than it says.
- **An ambiguous target** — two channels loosely matching a name, several plausible senders. Ask instead of picking.

## Red Flags

- Sending an OData parameter to a Teams endpoint without having read the Teams table this session.
- Explaining an error by reasoning about Graph instead of reading the reference.
- Setting `fetchAllPages` "to be safe".
- Reporting a channel as quiet from a channel-message listing — that call returns root messages only, never replies.
- Declaring a message missing after one search, without trying the alternate spelling, the sender's address form, or a folder-scoped call.
