# Webhooks

A webhook is a way for an API or application to send real-time data to another system when a specific event occurs. Instead of you polling an API every 5 minutes, a webhook pushes data to you automatically when something important happens.

## How Webhooks Work (Basic Flow)
1. You register your callback URL (e.g. `https://yourapp.com/webhook`).
2. The third-party API (Stripe, GitHub, etc.) stores your URL.
3. When an event happens (like a new payment or repo push), it:
4. Sends an HTTP POST request to your webhook endpoint.
5. Includes event data (JSON) in the body.
6. Your server receives the event and handles it (e.g., logs, stores, triggers ETL).

## Testing Webhooks

Tools:
* [Webhook.site](https://webhook.site/#!/view/3ce19d65-3ae2-4340-8fcf-5a5910a1fefa)	Receive and inspect webhook payloads
* [Ngrok](https://ngrok.com/)	Expose local server to the internet
* Postman Mock Servers	Simulate an endpoint and trigger actions
* Beeceptor	Inspect and debug HTTP requests
* Localhost.run or Expose	Ngrok alternatives

Example: Test a webhook locally with Ngrok
```
python -m http.server 5000  # Or use Flask/Node/etc.
ngrok http 5000
```
Ngrok gives you a public URL like:

```
https://abc123.ngrok.io/webhook
```

Register that URL in the external service as your webhook endpoint.
