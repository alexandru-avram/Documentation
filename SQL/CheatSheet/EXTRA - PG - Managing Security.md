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

### Database & Schema Level Security

Database: control CONNECT privileges.

```
REVOKE CONNECT ON DATABASE mydb FROM PUBLIC;
GRANT CONNECT ON DATABASE mydb TO analyst;
```

Schema: control USAGE and CREATE.

```
GRANT USAGE ON SCHEMA analytics TO analyst;
GRANT CREATE ON SCHEMA analytics TO data_engineer;
```

### Table & Column Level Security

Table level: `SELECT`, `INSERT`, `UPDATE`, `DELETE` rights.

```
GRANT SELECT, INSERT ON sales.orders TO analyst;
```

Column level: restrict sensitive fields (e.g., salary).

```
GRANT SELECT (name, department) ON employees TO analyst;
```

### Row Level Security (RLS)

Powerful feature: enforce row visibility with policies. You can tie RLS to `CURRENT_USER` or application variables.

```
ALTER TABLE orders ENABLE ROW LEVEL SECURITY;

CREATE POLICY region_policy
ON orders
FOR SELECT
USING (region = current_setting('app.region'));
```

## Policies (Creating, Dropping, Inspecting)

```
CREATE POLICY policy_name
ON table_name
FOR SELECT
USING (condition);
```

```
DROP POLICY policy_name ON table_name;
```

Inspect policies:
```
\d+ table_name   -- in psql
```

## Encryption

- At-rest: handled by disk/OS-level encryption (not Postgres-specific).
- In-transit: SSL/TLS (`ssl=on` in `postgresql.conf`).
- In-columns: use `pgcrypto` extension:

```
CREATE EXTENSION pgcrypto;

INSERT INTO users (id, email_enc)
VALUES (1, pgp_sym_encrypt('alex@example.com', 'secretkey'));

SELECT pgp_sym_decrypt(email_enc::bytea, 'secretkey')
FROM users;
```
