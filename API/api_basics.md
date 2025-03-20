# API Basics

## What is an API

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


## 2. Types of APIs
* **REST** (Representational State Transfer) APIs → Most common, follows HTTP rules.
* **SOAP** (Simple Object Access Protocol) APIs → More structured, uses XML.
* **GraphQL APIs** → Allows fetching only required data (flexible queries).
* **WebSockets APIs** → Real-time communication (e.g., chat applications).


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
* **HTTP Method	Defines the action (GET, POST, PUT, DELETE, etc.).
* **Headers**	Metadata sent with the request (e.g., authentication, content type).
* **Body (Payload)**	Data sent with POST/PUT requests (usually in JSON or XML format).
* **Query Parameters**	Key-value pairs appended to the URL to modify the request.
* **Path Parameters**	Variables within the URL that specify resources.

APIs have structured endpoints that define resources and actions.

Example API Endpoint Structure
```
https://api.example.com/users/{user_id}/orders
```

* https://api.example.com/ → Base URL
* /users/{user_id}/orders → Resource Path
* `{user_id}` → Path Parameter




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
