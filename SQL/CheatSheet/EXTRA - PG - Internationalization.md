# Internationalization (i18n) & Localization (l10n)

Sometimes people say internalization when they mean internationalization.

PostgreSQL has built-in support for:
- Character encodings (UTF-8, Latin1, etc.)
- Collations (rules for sorting text depending on locale, e.g. en_US, ro_RO)
- Date/time formatting in different languages.

UTF8 is strongly recommended for almost all modern PostgreSQL setups.

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

## Server Encoding

- Server encoding is the character set PostgreSQL uses internally to store text (CHAR, VARCHAR, TEXT).
- If you want to handle English, Romanian, German, Japanese, Arabic all in one database → you need an encoding that supports all characters.
- It determines how bytes are interpreted as characters.

Example: UTF8 vs. LATIN1 → same bytes may represent different characters.

```
SHOW SERVER_ENCODING;
```

When creating a database, you can specify:
```
CREATE DATABASE mydb
  ENCODING 'UTF8'
  LC_COLLATE='ro_RO.UTF-8'
  LC_CTYPE='ro_RO.UTF-8'
  TEMPLATE=template0;
```
- `ENCODING` = how text is stored (UTF8, LATIN1, WIN1252, etc.).
- `LC_COLLATE` = how text is sorted (dictionary order, accents, locale rules).
- `LC_CTYPE` = character classification (uppercase/lowercase rules, e.g. ß in German → SS in uppercase).


| Encoding    | Use Case                                                                          |
| ----------- | --------------------------------------------------------------------------------- |
| `UTF8`      | ✅ Best choice, supports all Unicode. Standard for multi-language systems.         |
| `LATIN1`    | Western Europe (legacy).                                                          |
| `WIN1252`   | Windows apps, legacy text files.                                                  |
| `SQL_ASCII` | ⚠️ Dangerous (no validation, can store invalid bytes). Avoid unless you know why. |
