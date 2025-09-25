# Managing PostgreSQL Security

## Security Concepts and Levels

Security applies at multiple layers:
- **Instance level** → Who can connect to the server? (`pg_hba.conf`, roles).
- **Database level** → Which databases can they access?
- **Schema level** → Which namespaces (schemas) inside a DB can they use?
- **Table level** → Which tables/views can they query?
- **Column level** → Restrict access to sensitive fields.
- **Row level** → Policies filtering which rows a user can see.

### Instance Level Security

Managed via Postgres roles (users & groups). Defined in `pg_hba.conf` for authentication (password, trust, SSL).

```
CREATE ROLE analyst LOGIN PASSWORD 'secret';
GRANT CONNECT ON DATABASE sales TO analyst;
```

