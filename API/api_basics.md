# API Basics

## 1. What is an API

An API defines a set of rules that allow one application to interact with another.
APIs enable:
* Data exchange between applications.
* Automation of tasks.
* Integration of third-party services (e.g., Payment gateways, Weather APIs).

**Analogy**:
Think of an API as a waiter in a restaurant:

* The client (you) orders food.
* The API (waiter) takes your order to the server (kitchen).
* The server prepares the food and sends it back via the API.

<br>

## 2. Types of APIs
* **REST** (Representational State Transfer) APIs → Most common, follows HTTP rules.
* **SOAP** (Simple Object Access Protocol) APIs → More structured, uses XML.
* **GraphQL APIs** → Allows fetching only required data (flexible queries).
* **WebSockets APIs** → Real-time communication (e.g., chat applications).

<br>

## 3. Request & Response Structure
APIs exchange data using requests and responses.

API Request Example (GET request to fetch user data)
```
GET https://api.example.com/users/123
Headers:
  Authorization: Bearer YOUR_TOKEN
  Accept: application/json
```

API Response Example (JSON format)
```
{
  "id": 123,
  "name": "John Doe",
  "email": "johndoe@example.com"
}
```

An API request consists of the following components:

* **Endpoint (URL)**	The address where the API is hosted (e.g., https://api.example.com/users).
* **HTTP Method**	Defines the action (GET, POST, PUT, DELETE, etc.).
* **Headers**	Metadata sent with the request (e.g., authentication, content type).
* **Body (Payload)**	Data sent with POST/PUT requests (usually in JSON or XML format).
* **Query Parameters**	Key-value pairs appended to the URL to modify the request.
* **Path Parameters**	Variables within the URL that specify resources.

#### Endpoints & Paths
APIs have structured endpoints that define resources and actions.

Example API Endpoint Structure
```
https://api.example.com/users/{user_id}/orders
```
* https://api.example.com/ → Base URL
* /users/{user_id}/orders → Resource Path
* `{user_id}` → Path Parameter


#### Query Parameters
Query parameters are key-value pairs added to the URL to filter or modify the request.

Query Parameter Example
```
GET https://api.example.com/users?age=25&status=active
```
* `?age=25` Filters users who are 25 years old.
* `&status=active`  Filters users who are active.

Common use cases
* `?limit=10`	Limits results to 10 records.
* `?sort=asc`	Sorts data in ascending order.
* `?filter=category:books`	Filters data by category.
* `?fields=name,email`	Returns only the name and email fields.


#### Path Parameters
Path parameters are variables within the URL that identify specific resources.

```
GET https://api.example.com/users/123
```
* `{user_id} = 123` Fetches details for user 123.

Example with multiple parameters
```
GET https://api.example.com/users/123/orders/456
```
* `{user_id} = 123` Fetches orders for user 123.
* `{order_id} = 456` Retrieves order 456.

#### Path Parameters vs. Query Parameters

* **Path Parameter**	Used for identifying a specific resource (/users/123).
* **Query Parameter**	Used for filtering, sorting, or modifying data (?limit=10).


#### Request Headers
Headers provide metadata about the request, such as authentication details and content type.

Common API Headers
* **Authorization**	Sends API keys or tokens.	`Bearer YOUR_ACCESS_TOKEN`
* **Content-Type**	Defines the request body format.	`application/json`
* **Accept**	Specifies the expected response format.	`application/json`
* **User-Agent**	Identifies the client making the request.	`PostmanRuntime/7.29.0`


#### Response Headers
Similar to request headers, response headers provide useful information.

* **Content-Type**	Defines the response format.	`application/json`
* **Cache-Control**	Controls caching behavior.	`no-cache`
* **RateLimit-Limit**	API rate limit.	`1000 requests/hour`

<br>

## 4. Rest API Methods
REST APIs use standard **HTTP methods** to perform operations on resources.

* **GET**	Retrieve data from a server
* **POST**	Send data to the server (create new resources)
* **PUT**	Update an entire existing resource
* **PATCH**	Partially update an existing resource
* **DELETE**	Remove a resource from the server

## 5. HTTP Status Codes
Every API request gets a response with a status code.

* **200 OK**	Request was successful
* **201 Created**	New resource was created
* **400 Bad Request**	Client error (e.g., missing required fields)
* **401 Unauthorized**	Authentication required
* **403 Forbidden**	Access denied
* **404 Not Found**	Requested resource doesn’t exist
* **500 Internal Server Error**	Server issue

## 6. API Authentication Methods
APIs often require authentication to ensure secure access.

* **API Key**	A unique key (sent in headers or URL)
* **OAuth 2.0**	Token-based authentication for secure access
* **JWT (JSON Web Token)**	Encoded user info for session-based authentication
* **Basic Auth**	Username & password (encoded in Base64)

## 7. Pagination
APIs return data in chunks to avoid overloading the server or client.

**Examples**:
* `?page=2&limit=20`: Page-based pagination
* `?offset=40&limit=20`: Offset-based pagination
* `?cursor=abc123`: Cursor-based (best for real-time data, like Twitter)

## 8. Rate Limiting & Retry Strategies
Rate limiting controls how many API requests a client can make in a given time frame. Most APIs return an `HTTP 429 – Too Many Requests` status code when you exceed your rate.

Rate limiting headers to watch:
* `X-RateLimit-Limit`:	Max requests per period
* `X-RateLimit-Remaining`:	How many requests left
* `X-RateLimit-Reset`:	When limit resets (UNIX timestamp)
* `Retry-After`:	Seconds until retry allowed

Retries are used when the error is transient (temporary) — like a 429 or 500.
