# Postgres - Crosstab Reports

In PostgreSQL, crosstab reports (via the `tablefunc` extension) let you pivot data—turning rows into columns.

```
CREATE EXTENSION IF NOT EXISTS tablefunc;
```

This gives you access to the `crosstab()` function.

## Basic Syntax

```
SELECT *
FROM crosstab(
  'SELECT col1, col2, col3
   FROM my_table
   ORDER BY col1, col2'
) 
AS ct(col1 TEXT, col2_val INT, col3_val INT);
```

- `col1` → row identifier (e.g., user, product)
- `col2` → pivot/category column (e.g., month, status)
- `col3` → value/measure (e.g., count, sum, amount)


## Fixed Categories (Manual Definition)

```
SELECT *
FROM crosstab(
  'SELECT col1, col2, col3
   FROM my_table
   ORDER BY col1, col2'
) 
AS ct(col1 TEXT, categoryA INT, categoryB INT, categoryC INT);
```

## Dynamic Categories (Using a Category SQL)

```
SELECT *
FROM crosstab(
  $$
  SELECT col1, col2, col3
  FROM my_table
  ORDER BY col1, col2
  $$,
  $$
  SELECT DISTINCT col2
  FROM my_table
  ORDER BY col2
  $$
) 
AS ct(col1 TEXT, categoryA INT, categoryB INT, categoryC INT);
```

## Best practices

- Always `ORDER BY col1, col2` in the source query.
- You must explicitly declare output columns (categoryX, categoryY...).
- Missing categories show up as NULL.
- Works best when you know or control the category list.
