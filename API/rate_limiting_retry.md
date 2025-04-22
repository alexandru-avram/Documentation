#  Rate Limiting & Retry Strategies
Rate limiting controls how many API requests a client can make in a given time frame. Most APIs return an `HTTP 429 – Too Many Requests` status code when you exceed your rate.

Example of API Response:
```
{
  "error": "Rate limit exceeded",
  "retry_after": 30
}
```

Rate limiting headers to watch:
* `X-RateLimit-Limit`:	Max requests per period
* `X-RateLimit-Remaining`:	How many requests left
* `X-RateLimit-Reset`:	When limit resets (UNIX timestamp)
* `Retry-After`:	Seconds until retry allowed

Retries are used when the error is transient (temporary) — like a 429 or 500:
* 429 Too Many Requests
* 502 Bad Gateway
* 503 Service Unavailable
* 504 Gateway Timeout

## Retry Strategy Types
1. Immediate Retry (Not Recommended): Retry immediately — can amplify failures.
2. Fixed Delay: wait 5 seconds → retry
3. Exponential Backoff: Widely used by Google, AWS, etc. Gives servers time to recover.
4. Exponential Backoff with Jitter: `delay = (2^retryAttempt) + random_ms`

## Best Practices:

* Use API-provided rate headers
* Throttle your requests (don’t just spam a loop)
* Implement backoff & retries
* Log 429s & retry attempts
* Cache successful data responses to avoid refetching
