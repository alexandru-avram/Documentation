# Internationalization (i18n) & Localization (l10n)

Sometimes people say internalization when they mean internationalization.

PostgreSQL has built-in support for:
- Character encodings (UTF-8, Latin1, etc.)
- Collations (rules for sorting text depending on locale, e.g. en_US, ro_RO)
- Date/time formatting in different languages.

So if you read internalization, it may be shorthand for making Postgres work with multiple languages and locales.

```
CREATE DATABASE mydb
LC_COLLATE='ro_RO.UTF-8'
LC_CTYPE='ro_RO.UTF-8'
TEMPLATE=template0;
```

## Internalization of Queries (Execution)

Inside Postgres’ engine, internalization sometimes refers to how SQL statements get transformed into internal data structures during parsing and planning:
- Parse Tree → SQL text is turned into a tree structure.
- Query Tree → semantic checks applied (do the tables/columns exist?).
- Planner/Optimizer → internal representation is generated, joins reordered, indexes considered.
- Execution Plan → final internal steps (sequential scan, index scan, hash join, etc.).

In this sense, internalization means “turning SQL into Postgres’ internal execution logic”.

## Internal Data Storage Representation

- Another angle: Postgres internalizes data types into its own binary format for efficiency:
- TEXT stored in varlena (variable-length) format internally.
- NUMERIC stored with a base-10 digit array.
- JSONB stored in a binary tree-like structure for fast search.

So when you insert data, Postgres internalizes it → i.e., converts external input ('123.45') into internal storage format.
