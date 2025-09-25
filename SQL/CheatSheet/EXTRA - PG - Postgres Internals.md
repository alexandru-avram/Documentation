# Postgres Internals

## List database users, and database sizes

```
-- Users
\du
SELECT usename FROM pg_user;

-- Database sizes
SELECT pg_database.datname,
       pg_size_pretty(pg_database_size(datname)) AS database_size
FROM pg_database;
```

## List all databases and schemas

```
SELECT catalog_name as "Database Name"
FROM information_schema.information_schema_catalog_name
```

```
SELECT
*
FROM information_schema.schemata
WHERE schema_name LIKE 'pg%'
```

### List all tables

```
SELECT *
FROM information_schema.tables
WHERE table_schema IN ('public', 'information_schema')
```

```
SELECT table_name, table_schema
FROM information_schema.tables
WHERE table_schema NOT IN ('pg_catalog','information_schema');
```

### List all columns

```
SELECT 
column_name, table_name, data_type, dtd_identifier
FROM information_schema.columns
```

### View system metadata

```
SELECT
  CURRENT_CATALOG,
  CURRENT_DATABASE(),
  CURRENT_SCHEMA,
  CURRENT_USER,
  SESSION_USER;
```

```
SELECT VERSION();
```

### View privilages

```
SELECT grantee, privilege_type, table_name
FROM information_schema.role_table_grants
WHERE table_schema = 'public';
```

```
SELECT
  has_database_privilege('hr', 'CREATE'),
  has_schema_privilege('public', 'USAGE'),
  has_table_privilege('employees', 'CREATE'),
  has_any_column_privilege('countries', 'SELECT');
```

### View all current running queries

```
SELECT pid, usename, datname, state, query
FROM pg_stat_activity;
```

### Terminate idle processes

```
SELECT pg_terminate_backend(pid)
FROM pg_stat_activity
WHERE state='idle' AND pid <> pg_backend_pid();`
```
