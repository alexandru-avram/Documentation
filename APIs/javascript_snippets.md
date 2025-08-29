 # Postman Test Script Cheat Sheet (JavaScript)

 ### 1. Check Status Code
 ```
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});
```

### 2. Check Response Time
```
pm.test("Response time is less than 500ms", function () {
    pm.expect(pm.response.responseTime).to.be.below(500);
});
```

### 3. Check Response is JSON
```
pm.test("Content-Type is JSON", function () {
    pm.response.to.have.header("Content-Type");
    pm.expect(pm.response.headers.get("Content-Type")).to.include("application/json");
});
```

### 4. Validate Response Body Content

**Example**: `userId` should be `1`

```
pm.test("userId is 1", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData.userId).to.eql(1);
});
```

**Example**: Validate an array length
```
pm.test("Has 10 items", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData.length).to.eql(10);
});
```

### 5. Validate Authentication
```
pm.test("Should be unauthorized", function () {
    pm.response.to.have.status(401);
});
```

### 6. Loop Through Array of Objects
```
pm.test("All users have an email", function () {
    let data = pm.response.json();
    data.forEach(user => {
        pm.expect(user).to.have.property("email");
    });
});
```

### 7. Set Environment or Global Variables from Response
```
let jsonData = pm.response.json();
pm.environment.set("authToken", jsonData.token);
pm.globals.set("userId", jsonData.id);
```

### 8. Use Variables in Request Body/Header
In body or header, the following JSON:

```
{
  "email": "{{user_email}}",
  "password": "{{user_password}}"
}
```

Set them in Pre-request Script:
```
pm.environment.set("user_email", "alex@example.com");
pm.environment.set("user_password", "1234");
```

### 9. Clear Variables After Test
```
pm.environment.unset("authToken");
```

### 10. Log Output to Postman Console
```
console.log("Response Body:", pm.response.text());
```

### 11. Advanced Assertions (Chai JS Syntax)
```
pm.expect(true).to.be.true;
pm.expect(10).to.be.above(5);
pm.expect("Alex").to.include("lex");
```
