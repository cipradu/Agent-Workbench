# Teams Queries

Covers `list-joined-teams`, `list-team-channels`, `list-channel-messages`, `list-channel-message-replies`, `list-chats`, `list-chat-messages`, `list-chat-members`, `list-team-members`.

**Teams endpoints reject most OData parameters.** This is the single largest source of `400`s in this server, because every tool advertises the full parameter set regardless. Consult the matrix before sending anything.

## Parameter Support Matrix

`Y` = documented as supported. `N` = documented as unsupported, or empirically confirmed to return `400`. `?` = not documented either way — treat as unsupported and shape client-side.

| Endpoint (tool) | top | skip | filter | select | expand | orderby | search | count |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `/me/joinedTeams`<br>`list-joined-teams` | **N** | N | N | **N** | N | N | N | N |
| `/teams/{id}/channels`<br>`list-team-channels` | **N** | ? | Y | **Y** | ? | ? | ? | ? |
| `/teams/{id}/channels/{id}/messages`<br>`list-channel-messages` | **Y** | N | N | **N** | Y | **N** | N | N |
| `…/messages/{id}/replies`<br>`list-channel-message-replies` | Y | N | N | N | N | N | N | N |
| `/me/chats`<br>`list-chats` | Y | ? | Y | ? | Y | Y | ? | ? |
| `/chats/{id}/messages`<br>`list-chat-messages` | Y | N | Y | ? | ? | Y | N | N |
| `/chats/{id}/members`<br>`list-chat-members` | N | N | N | N | N | N | N | N |
| `/teams/{id}/members`<br>`list-team-members` | Y | ? | ? | ? | ? | ? | ? | ? |

Bolded cells are the ones agents get wrong most often.

Value limits where a parameter *is* supported:

- `top` on channel messages: default 20, **maximum 50**
- `top` on replies, chats, chat messages: **maximum 50**
- `top` on team members: supported, maximum undocumented
- `orderby` on chats and chat messages: **descending only**; ascending is not supported
- `expand` on channel messages: `replies`
- `expand` on chats: `members`, `lastMessagePreview`

Sources: https://learn.microsoft.com/en-us/graph/api/user-list-joinedteams · https://learn.microsoft.com/en-us/graph/api/channel-list · https://learn.microsoft.com/en-us/graph/api/channel-list-messages · https://learn.microsoft.com/en-us/graph/api/chatmessage-list-replies · https://learn.microsoft.com/en-us/graph/api/chat-list · https://learn.microsoft.com/en-us/graph/api/chat-list-messages · https://learn.microsoft.com/en-us/graph/api/chat-list-members

## The Three Common Failures

**`list-joined-teams` takes no parameters at all.** Not `top`, not `select`. The endpoint is documented as supporting none, and `top` returns `400 Query option 'Top' is not allowed`. Call it bare and truncate the result yourself — including when the user says "just the first five".

```
list-joined-teams  { }
```

**`list-team-channels` accepts `select` but not `top`.** Trim fields, do not page.

```
list-team-channels  { teamId: "<id>", select: "id,displayName" }
```

`select` matters here beyond context size: populating a channel's `email` property is an expensive server-side operation, so excluding it measurably speeds the call.

**`list-channel-messages` accepts only `top` and `expand`.** No `select`, no `orderby`, no `filter`. Messages come back newest-first by default.

```
list-channel-messages  { teamId: "<id>", channelId: "<id>", top: 5 }
```

## chatMessage Has No bodyPreview

The mail `message` resource has `bodyPreview`. The Teams `chatMessage` resource does not. Requesting it returns:

```
400  Could not find a property named 'bodyPreview' on type 'microsoft.graph.chatMessage'
```

Message text lives in `body.content`, with `body.contentType` either `text` or `html`. It is always `html` when the message contains a mention. To show a preview, take `body.content` and truncate it yourself.

Since `select` is unsupported on channel messages anyway, the full message object is returned regardless — keep `top` small to control size.

Source: https://learn.microsoft.com/en-us/graph/api/resources/chatmessage

## Root Messages vs Replies

`list-channel-messages` returns **root messages only**. Replies are not included.

A thread with one root post and forty replies appears in that listing as a single message. Never report a channel as quiet, or summarize its activity, from this call alone.

Two ways to get replies:

- `expand: "replies"` on `list-channel-messages` — nested, one call
- `list-channel-message-replies` per root message — separate call, `top` up to 50

`replyToId` on a message is non-null when it is a reply.

**Known Microsoft bug:** paging replies via `@odata.nextLink` can return an empty array while more results exist. Root cause unconfirmed. If replies come back empty on page 2+, do not conclude there are none — say the listing is unreliable.

Source: https://learn.microsoft.com/en-us/graph/api/chatmessage-list-replies

## Finding a Chat

`chatType` distinguishes one-to-one from group chats. Filtering chats by member is **not documented** — list with `list-chats` and match participants client-side.

`expand: "members"` returns at most **25 members**, regardless of `top`. For a larger chat, call `list-chat-members` separately — which accepts no parameters and returns everyone in one response.

For a meeting chat, take `chatInfo.threadId` from `get-online-meeting` and use it as the `chatId`.

## Date Filtering

Asymmetric between chats and channels:

- **Chat messages — supported.** `filter` on `lastModifiedDateTime` or `createdDateTime`, ISO 8601 UTC.
  ```
  filter: "lastModifiedDateTime gt 2026-07-25T00:00:00.000Z and lastModifiedDateTime lt 2026-08-01T00:00:00.000Z"
  ```
- **Channel messages — not supported.** Date filtering requires `getAllMessages`, which needs application permissions most delegated sessions do not have. With delegated auth, page with `top` and filter by `createdDateTime` client-side.

## Delta

Delta on Teams message endpoints is **not documented for v1.0**. Do not assume it exists. Use `top` plus client-side date comparison instead.

## Permissions

`403` here is a consent problem, not a query problem. Report the scope; changing parameters will not help.

| Operation | Delegated scope |
| --- | --- |
| List joined teams | `Team.ReadBasic.All` |
| List channels | `Channel.ReadBasic.All` |
| Read channel messages | `ChannelMessage.Read.All` |
| List chats | `Chat.ReadBasic` / `Chat.Read` |
| Read chat messages | `Chat.Read` |
| List members | `TeamMember.Read.All` |

`ChannelMessage.Read.All` requires admin consent, so it is the most common `403` for an ordinary user. Application-only access to Teams messages is not available outside migration scenarios — a `403` saying the calling application is not authorized means delegated auth is required.

Source: https://learn.microsoft.com/en-us/graph/permissions-reference

## Throttling

Teams limits are tighter than mail:

| Operation | Delegated limit |
| --- | --- |
| Read channel or chat messages | 20 requests/sec, and 1/sec per user |
| List teams | 30 requests/sec |
| Other Teams reads | 30 requests/sec |

The per-user limit of 1 request/sec on message reads is the practical constraint: fanning out across many channels will throttle. Sequence the calls and keep `top` small rather than issuing many parallel reads.

On `429`, honor `Retry-After` exactly.

Source: https://learn.microsoft.com/en-us/graph/throttling-limits

## Message History

Neither endpoint documents a hard history cutoff; how far back messages go depends on tenant retention policy. For bulk historical extraction Microsoft directs users to Graph Data Connect rather than these REST endpoints — if a user asks to export a channel's full history, say that these tools are the wrong instrument rather than paging indefinitely.

## Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `400 Query option 'Top' is not allowed` | `top` on `joinedTeams` or `channels` | Remove it; truncate client-side |
| `400 Could not find a property named 'bodyPreview'` | `select` with a mail-only property | Use `body.content` |
| `400` on `select` for channel messages | `select` unsupported on that endpoint | Drop it; keep `top` small |
| `400` on `orderby` ascending | Only descending is supported | Remove `orderby`; reverse client-side |
| Empty replies on page 2+ | Known Microsoft paging bug | Report as unreliable, not as zero |
| `403 Insufficient privileges` | Missing scope or admin consent | Name the scope; stop |
| `429` | Throttled — likely parallel message reads | Honor `Retry-After`; serialize calls |
