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


## 3. Rest API Fundamentals
REST APIs use standard **HTTP methods** to perform operations on resources.

* **GET**	Retrieve data from a server
* **POST**	Send data to the server (create new resources)
* **PUT**	Update an entire existing resource
* **PATCH**	Partially update an existing resource
* **DELETE**	Remove a resource from the server

## 4. HTTP Status Codes
Every API request gets a response with a status code.

* **200 OK**	Request was successful
* **201 Created**	New resource was created
* **400 Bad Request**	Client error (e.g., missing required fields)
* **401 Unauthorized**	Authentication required
* **403 Forbidden**	Access denied
* **404 Not Found**	Requested resource doesn’t exist
* **500 Internal Server Error**	Server issue


## 5. 5. Request & Response Structure
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


## 6. 6. API Authentication Methods
APIs often require authentication to ensure secure access.

* **API Key**	A unique key (sent in headers or URL)
* **OAuth 2.0**	Token-based authentication for secure access
* **JWT (JSON Web Token)**	Encoded user info for session-based authentication
* **Basic Auth**	Username & password (encoded in Base64)
