# Python API Testing Cheat Sheet
Library used: `requests`

Other liberies:
* pytest	Advanced test cases
* responses	Mock HTTP responses
* httpx	Async HTTP client
* pydantic	Schema validation
* jsonschema	Validate API responses

### Make a GET Resuest
```
import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(response.status_code)
print(response.json())
```

### POST Request with JSON Payload
```
payload = {"title": "foo", "body": "bar", "userId": 1}
headers = {"Content-Type": "application/json"}

response = requests.post("https://jsonplaceholder.typicode.com/posts", json=payload, headers=headers)
print(response.status_code)
```

### PUT / PATCH Request
```
payload = {"title": "Updated Title"}
response = requests.patch("https://jsonplaceholder.typicode.com/posts/1", json=payload)
```

### DELETE Request
```
response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
print(response.status_code)  # Should be 200 or 204
```

### API Key or Bearer Token Authentication
```
headers = {"Authorization": "Bearer YOUR_TOKEN"}
requests.get("https://api.example.com/protected", headers=headers)
```

### Validate Status Code
```
assert response.status_code == 200, "Status code is not 200!"
```

### Validate Response JSON
```
data = response.json()
assert data["userId"] == 1
assert "title" in data
```

### Handle Pagination
```
results = []
page = 1

while True:
    res = requests.get(f"https://api.example.com/items?page={page}")
    data = res.json()
    if not data:
        break
    results.extend(data)
    page += 1
```

### Retry Strategy with Backoff
```
import time

for i in range(5):
    res = requests.get("https://api.example.com/resource")
    if res.status_code == 200:
        break
    time.sleep(2 ** i)  # Exponential backoff
```

### Log Details for Debugging
```
print("Status Code:", res.status_code)
print("Headers:", res.headers)
print("Body:", res.text)
```

### Basic Unit Test Template
```
import unittest

class TestAPI(unittest.TestCase):
    def test_get_post(self):
        res = requests.get("https://jsonplaceholder.typicode.com/posts/1")
        self.assertEqual(res.status_code, 200)
        self.assertIn("userId", res.json())

if __name__ == "__main__":
    unittest.main()
```

12. Save API Response to File
```
with open("response.json", "w") as f:
    f.write(res.text)
```
