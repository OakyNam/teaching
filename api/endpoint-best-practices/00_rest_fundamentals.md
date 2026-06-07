# REST Fundamentals

## What REST Is
REST (Representational State Transfer) is an architectural style for distributed systems described by Roy Fielding. In practice, it means exposing resources over HTTP with predictable URLs, uniform message formats, and standard method semantics.

A client does **not** manipulate the server's internal objects directly. Instead, it transfers representations of resources such as JSON documents:

- `GET /books/42` returns a representation of book `42`
- `PUT /books/42` replaces that representation
- `DELETE /books/42` removes that resource

REST is popular because it uses the web's existing rules instead of inventing a custom protocol for every API.

## The 6 REST Constraints
1. **Client-server**  
   Separate UI concerns from data/storage concerns. Clients can evolve independently from servers.
2. **Stateless**  
   Every request contains all information needed to process it. The server should not rely on hidden per-client session state.
3. **Cacheable**  
   Responses should define whether they can be cached. This reduces latency and server load.
4. **Uniform interface**  
   Resources are identified by URLs, manipulated through representations, use self-descriptive messages, and may include hypermedia links.
5. **Layered system**  
   Clients do not need to know whether they are talking to the origin server, a proxy, a gateway, or a cache.
6. **Code on demand (optional)**  
   Servers may send executable code to clients, though most modern APIs do not rely on this.

The **uniform interface** is what makes REST feel different from ad hoc HTTP APIs.

## HTTP Methods And Semantics

### GET
- Read-only
- **Safe**: should not change server state
- **Idempotent**: repeating it should produce the same effect on state
- Typical uses: fetch a collection or single resource

Example:
```http
GET /books/42 HTTP/1.1
Accept: application/json
```

```http
HTTP/1.1 200 OK
Content-Type: application/json

{"id": 42, "title": "REST in Practice"}
```

> Do not use `GET` to trigger writes like "mark as read", "increment download count", or "delete". Logging and metrics are acceptable side effects; business state mutations are not.

### POST
- Usually used to create a subordinate resource or trigger a non-idempotent action
- **Not idempotent** by default
- Repeating the same POST may create duplicates unless you add an idempotency key policy

Example:
```http
POST /books HTTP/1.1
Content-Type: application/json

{"title": "API Design", "author": "Sam"}
```

```http
HTTP/1.1 201 Created
Location: /books/43
Content-Type: application/json

{"id": 43, "title": "API Design", "author": "Sam"}
```

### PUT
- Full update or replacement of a resource representation
- **Idempotent**
- Sending the same full representation multiple times should leave the resource in the same final state

Example:
```http
PUT /books/43 HTTP/1.1
Content-Type: application/json

{"title": "API Design, 2nd Edition", "author": "Sam", "in_stock": true}
```

### PATCH
- Partial update
- Sends only the fields being changed
- Can be idempotent or non-idempotent depending on patch semantics, but most JSON merge-style PATCH operations are designed to be idempotent

Example:
```http
PATCH /books/43 HTTP/1.1
Content-Type: application/merge-patch+json

{"in_stock": false}
```

### DELETE
- Removes a resource
- **Idempotent**: deleting an already-deleted resource should not create additional state changes
- Often returns `204 No Content`

Example:
```http
DELETE /books/43 HTTP/1.1
```

```http
HTTP/1.1 204 No Content
```

### HEAD
- Same semantics as `GET`, but no response body
- Useful for metadata checks, content length, or cache validation

### OPTIONS
- Returns supported methods or CORS-related metadata
- Often used by browsers during CORS preflight requests

## HTTP Status Codes By Category

### 2xx Success
- **200 OK** — standard successful read or update response
- **201 Created** — new resource created successfully; typically include `Location`
- **204 No Content** — success with no body, common for `DELETE` or `HEAD`

### 3xx Redirection
- **301 Moved Permanently** — permanent redirect
- **302 Found** — temporary redirect (legacy semantics)

### 4xx Client Errors
- **400 Bad Request** — malformed syntax or invalid request structure
- **401 Unauthorized** — authentication required or failed
- **403 Forbidden** — authenticated but not allowed
- **404 Not Found** — resource does not exist
- **409 Conflict** — state conflict such as duplicate unique key or version mismatch
- **422 Unprocessable Entity** — syntactically valid request with semantic validation errors

### 5xx Server Errors
- **500 Internal Server Error** — unhandled server failure
- **502 Bad Gateway** — upstream dependency returned an invalid response
- **503 Service Unavailable** — temporary overload or maintenance

## URL Design Basics
Prefer resource nouns over verbs:

- Good: `/books`, `/books/42`
- Avoid: `/getBooks`, `/createBook`, `/deleteBookById`

Prefer plural collections:

- `/users`
- `/orders`
- `/invoices`

Use nested resources when the hierarchy is meaningful:

- `/customers/7/orders`
- `/customers/7/orders/99`

Keep URLs stable and push behavior into HTTP methods plus request bodies or query parameters.

## Request And Response Structure
Typical request parts:
- **Method**: `GET`, `POST`, etc.
- **Path**: `/books/42`
- **Query string**: `?limit=20&sort=title`
- **Headers**: metadata and negotiation
- **Body**: usually JSON for create/update operations

Important headers:
- **Content-Type** — describes the request or response format, such as `application/json`
- **Accept** — tells the server which response media type the client wants
- **Authorization** — sends credentials, often bearer tokens or API keys

Example:
```http
GET /books?limit=10 HTTP/1.1
Accept: application/json
Authorization: ******
```

## Safety And Idempotency
These concepts are related but different.

### Safe
A safe method should not change business state.
- `GET /books` is safe
- `HEAD /books` is safe
- `POST /books` is not safe

### Idempotent
An idempotent method can be repeated and the end state stays the same.
- `PUT /books/42` with the same body is idempotent
- `DELETE /books/42` is idempotent
- `POST /books` is not idempotent by default

Examples:
- Repeating `DELETE /books/42` three times still leaves the resource deleted.
- Repeating `POST /books` three times may create three books.
- Repeating `PATCH /books/42` with `{"status": "archived"}` is usually idempotent if it is merge-style patching.

## Richardson REST Maturity Model
The Richardson model describes increasing use of HTTP as an application protocol.

1. **Level 0: The Swamp of POX**  
   One endpoint, usually POST, remote-procedure style.
2. **Level 1: Resources**  
   Separate URLs identify resources such as `/books` and `/authors`.
3. **Level 2: HTTP Verbs**  
   Uses HTTP methods and status codes correctly (`GET`, `POST`, `PUT`, `DELETE`).
4. **Level 3: Hypermedia (HATEOAS)**  
   Responses include links describing valid next actions.

Example Level 3 response:
```json
{
  "id": 42,
  "title": "REST in Practice",
  "links": [
    {"rel": "self", "href": "/books/42"},
    {"rel": "author", "href": "/authors/9"},
    {"rel": "delete", "href": "/books/42", "method": "DELETE"}
  ]
}
```

## Practical Method Examples
- **GET /books** — list books, return `200`
- **GET /books/42** — fetch one book, return `200` or `404`
- **POST /books** — create a book, return `201` with `Location`
- **PUT /books/42** — replace a book, return `200` or `201` depending on creation policy
- **PATCH /books/42** — update just the changed fields, return `200`
- **DELETE /books/42** — remove book, return `204`
- **HEAD /books/42** — fetch metadata only, return `200`
- **OPTIONS /books/42** — advertise supported methods, return `204` or `200`

## REST Vs RPC Vs GraphQL

| Style | Strengths | Tradeoffs |
| --- | --- | --- |
| REST | Simple caching, clear HTTP semantics, familiar tooling, resource-oriented design | Can over-fetch or under-fetch without projection features; versioning can be awkward |
| RPC | Easy to model actions like `approveInvoice` or `sendPasswordReset` | Less uniform, often drifts into custom semantics over HTTP |
| GraphQL | Flexible client-driven queries, reduces over-fetching, single endpoint | More complex caching, authorization, observability, and query-cost control |

A practical system may mix styles:
- REST for core CRUD resources
- RPC-style endpoints for explicit commands
- GraphQL for complex UI composition queries

## Practical Guidance
- Use nouns for URLs and verbs for HTTP methods.
- Be strict about status codes.
- Never mutate domain state in `GET` handlers.
- Document whether operations are safe and idempotent.
- Use `PUT` for full replacement, `PATCH` for partial changes.
- Include examples of headers, request bodies, and responses in your API docs.
