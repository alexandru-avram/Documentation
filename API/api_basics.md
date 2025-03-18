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
