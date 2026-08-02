# Mail Queries

Covers `list-mail-messages`, `list-mail-folder-messages`, `get-mail-message`, `list-mail-folders`, `list-mail-child-folders`, `list-mail-attachments`, and the `list-shared-mailbox-*` equivalents.

Read the tool's own parameter descriptions for syntax. This file covers what they do not: limits, silent behaviors, and the choices between tools.

## Parameter Support

Unlike Teams, mail endpoints accept the full OData set. The constraints are on **combinations and values**, not on which parameters exist.

| Parameter | Supported | Constraint |
| --- | --- | --- |
| `search` | Yes | Cannot combine with `filter`. Cannot combine with `skip`. Caps at 1000 total results. |
| `filter` | Yes | Cannot combine with `search`. |
| `top` | Yes | Default page size 10, maximum **1000**. |
| `skip` | Yes | Works with `filter`, not with `search`. |
| `orderby` | Yes with `filter` | Interaction with `search` is **undocumented** — see below. |
| `select` | Yes | Always use it. |
| `expand` | Navigation properties only | `attachments` is the useful one on a message. |
| `count` | Yes | Set `true` for advanced filters (`contains()`, flag/flagStatus); sends `ConsistencyLevel: eventual`. |

Source: https://learn.microsoft.com/en-us/graph/api/user-list-messages

## Choosing the Tool

| Goal | Call |
| --- | --- |
| Find a message by keyword, sender, or subject across folders | `list-mail-messages` with `search` |
| Narrow by a structured property — unread, has attachments, date range | `list-mail-messages` with `filter` |
| Everything in one folder | `list-mail-folders` → then `list-mail-folder-messages` |
| Full body text of one message | `get-mail-message` with `messageId` |
| Someone else's or a shared mailbox | `list-shared-mailbox-messages`, passing the mailbox address as `userId` |

Listings return `bodyPreview` (first 255 characters). They do not return the full body. To read a message, take the `id` from the listing and call `get-mail-message`.

## Search vs Filter

They are mutually exclusive. Choose by what you are matching:

- **Text inside the message** — subject, body, sender name → `search`
- **A structured property** — `isRead`, `hasAttachments`, an exact date range → `filter`

If a task needs both ("unread mail from Sarah"), run the `search`, then narrow the returned set yourself. Do not attempt both parameters in one call.

### Search — KQL

`search` takes KQL, not OData. The value must be wrapped in double quotes.

Searchable prefixes: `from:`, `to:`, `cc:`, `bcc:`, `subject:`, `body:`, `attachment:`, `hasAttachments:`, `importance:`, `received:`, `sent:`, `participants:`, `recipients:`, `size:`, `kind:`

Boolean operators are case-sensitive and go outside quoted values: `AND`, `OR`.

```
search: "from:sarah@contoso.com"
search: "subject:invoice AND hasAttachments:true"
```

Two behaviors that are easy to get wrong:

- **Results are sorted by date sent, not relevance**, and cap at **1000 total**. Narrow the query rather than paging toward the cap.
- **Date syntax inside KQL differs from `filter`.** Microsoft documents KQL dates as `MM/DD/YYYY` (`received:07/23/2024`), while the server's own tool tip shows the ISO form (`received>=2024-01-01`). These conflict and the discrepancy is **unresolved**. Prefer `filter` with an ISO datetime for anything date-bounded; it is unambiguous. If you must use a date inside `search`, try one form and treat an empty result as inconclusive rather than as "no such mail".

Combining `orderby` with `search` is **undocumented** — Microsoft states neither support nor rejection. Omit `orderby` when using `search` and sort client-side.

Source: https://learn.microsoft.com/en-us/graph/search-query-parameter

### Filter — OData

Operators: `eq`, `ne`, `gt`, `ge`, `lt`, `le`, `and`, `or`, `not()`, `startswith()`, `endswith()`, `contains()`

```
filter: "isRead eq false"
filter: "receivedDateTime ge 2026-07-25T00:00:00Z and receivedDateTime lt 2026-08-01T00:00:00Z"
filter: "from/emailAddress/address eq 'sarah@contoso.com'"
filter: "categories/any(c:c eq 'Work')"
```

Constraints:

- **Datetime literals must be ISO 8601 with a trailing `Z`.** `2026-07-25` alone or a missing `Z` fails.
- **`eq` on a string is limited to 120 characters.** Use `contains()` for longer values, with `count: true`.
- **`bodyPreview` is not filterable.** `filter: "bodyPreview eq …"` returns `400 Invalid filter keys found: bodyPreview`. Search the body instead.
- Collection properties (`categories`, `toRecipients`) require the `any()` lambda.
- `contains()` and flag filters require `count: true`.

Source: https://learn.microsoft.com/en-us/graph/filter-query-parameter

## Dates and Time Zones

- **Filters are always UTC.** Express ranges as explicit ISO boundaries. "Today" and "last week" have no server-side meaning — compute the boundaries and pass them.
- **The `timezone` parameter** (on endpoints that support it) sets `Prefer: outlook.timezone` and changes **how datetimes are rendered in the response only**. It does not shift filter interpretation.
- It accepts **either** Windows identifiers (`Pacific Standard Time`) or IANA names (`America/Los_Angeles`). `/me/outlook/supportedTimeZones` lists valid values in either standard.

Source: https://learn.microsoft.com/en-us/graph/api/outlookuser-supportedtimezones

## Folders

Well-known names work as a folder id, with no lookup call: `inbox`, `drafts`, `sentitems`, `deleteditems`, `archive`, `junkemail`.

```
list-mail-folder-messages  { mailFolderId: "inbox", filter: "isRead eq false", top: 15 }
```

For a user-created folder, call `list-mail-folders` and match on `displayName` to get the id. Note that a user-created folder literally named "Archive" is a **different folder** from the well-known `archive` — if the distinction matters, resolve explicitly and compare `totalItemCount`.

Nested folders hang off `childFolders`; use `list-mail-child-folders` with the parent id.

Folder ids are stable across renames and moves.

## Message Bodies

| Property | Contains |
| --- | --- |
| `bodyPreview` | First 255 characters, always plain text. Returned by listings. |
| `body` | Full content. `{ contentType, content }`. |
| `uniqueBody` | Only the part unique to this message — strips quoted and forwarded text. Best for reading one reply in a long thread. |

**This server returns text, not HTML.** It sends `Prefer: outlook.body-content-type="text"` on every GET unless `MS365_MCP_BODY_FORMAT=html` is set. Do not write HTML-stripping logic for content that arrives as plain text.

For the raw RFC 5322 message, use `get-mail-message-mime`.

## Attachments

`list-mail-attachments` with `messageId`, or `expand: "attachments"` on `get-mail-message` for metadata inline.

Three types behave differently on download:

- `fileAttachment` — real bytes, downloadable
- `itemAttachment` — an attached Outlook item; returns MIME
- `referenceAttachment` — a link to OneDrive/SharePoint, **not** bytes. Downloading returns `405`; follow the URL through the file tools instead.

For anything above a few KB, prefer `get-download-url` over `download-bytes` — it returns a URL that streams straight to disk instead of routing base64 through the context.

## Paging

- Default page size is 10; `top` maximum is 1000. Both are far larger than a useful response — stay at 5–15 unless the task needs more.
- With `filter`, page using `skip`.
- With `search`, `skip` is unsupported. Follow `@odata.nextLink`, or narrow the query.
- `fetchAllPages: true` merges up to 100 pages automatically. Reserve it for explicit export requests.

## Message IDs

**Message ids change when a message moves between folders.** An id captured before a move may 404 afterward.

`Prefer: IdType="ImmutableId"` makes them stable, but must then be sent on *every* request — mixing modes yields two different ids for one message. Only relevant if ids are being persisted outside the session.

Source: https://learn.microsoft.com/en-us/graph/outlook-immutable-id

## Delta

`delta` tracks changes since a prior sync. Tokens **expire** — Outlook delta tokens age out of an internal cache. An expired token returns a `40X`, and the only recovery is a full resync from no token. Do not treat a stored delta token as permanently valid.

Delta cannot combine with `search`, `filter`, or `orderby`.

Source: https://learn.microsoft.com/en-us/graph/delta-query-overview

## Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `400 Invalid filter keys found: bodyPreview` | Filtering a non-filterable property | Use `search` for body text |
| `400` on a datetime comparison | Missing `Z`, or a date with no time component | Full ISO 8601 with `Z` |
| `400` with both `search` and `filter` present | Mutually exclusive | Pick one; narrow the rest client-side |
| `400` on a long `eq` string | Over the 120-character limit | `contains()` with `count: true` |
| Empty result from a KQL date query | Ambiguous KQL date format | Re-express as a `filter` range |
| `403` | Missing `Mail.Read` / `Mail.Read.Shared` | Report the scope; do not retry with other parameters |
| `429` | Throttled | Wait the `Retry-After` interval |
