# SQL Cheat Sheet

## Table of Contents
- [SELECT](#select)
  - [Basic SELECT](#basic-select)
  - [DISTINCT](#distinct)
  - [ORDER BY](#order-by)
  - [LIMIT](#limit)
- [CONDITIONS](#conditions)
  - [WHERE](#where)
  - [AND](#and)
  - [OR](#or)
  - [BETWEEN](#between)
  - [LIKE](#like)
  - [NULL](#null)
  - [NOT NULL](#not-null)
  - [IN](#in)
  - [NOT IN](#not-in)
  - [CASE](#case)
- [AGGREGATE FUNCTIONS](#aggregate-functions)
  - [COUNT](#count)
  - [SUM](#sum)
  - [AVG](#avg)
  - [MIN](#min)
  - [MAX](#max)
  - [GROUP BY](#group-by)
  - [HAVING](#having)
- [JOINS](#joins)
  - [INNER JOIN](#inner-join)
  - [LEFT JOIN](#left-join)
  - [RIGHT JOIN](#right-join)
  - [FULL OUTER JOIN](#full-outer-join)
- [SUBQUERIES](#subqueries)
  - [Scalar Subquery](#scalar-subquery)
  - [Correlated Subquery](#correlated-subquery)
- [CASE Statements](#case-statements)
- [UPDATE](#update)
- [DELETE](#delete)
- [INSERT INTO](#insert-into)
- [CREATE TABLE](#create-table)
- [ALTER TABLE](#alter-table)
- [INDEXES](#indexes)
- [TRANSACTIONS](#transactions)
  - [BEGIN TRANSACTION](#begin-transaction)
  - [COMMIT](#commit)
  - [ROLLBACK](#rollback)
- [VIEW](#view)
- [USER DEFINED FUNCTIONS](#user-defined-functions)
- [Stored Procedures](#stored-procedures)
- [TRIGGERS](#triggers)

---

## SELECT

### Basic SELECT
The basic SQL SELECT statement retrieves data from one or more tables.

```
SELECT column1, column2, ...
FROM table_name;
```


### DISTINCT
Removes duplicate records from the result set.

```
SELECT DISTINCT column1, column2, ...
FROM table_name;
```

### ORDER BY
Sorts the result set in ascending or descending order.

```
SELECT column1, column2, ...
FROM table_name
ORDER BY column1 [ASC|DESC];
```

### LIMIT
Limits the number of rows returned.

```
SELECT column1, column2, ...
FROM table_name
LIMIT number_of_rows;
```

## Conditions

### WHERE
Filters the records based on a condition.

```
SELECT column1, column2
FROM table_name
WHERE column1 = 'value';
```

### AND
Multiple conditions are used to filter records using AND.

```
SELECT column1, column2
FROM table_name
WHERE column1 = 'value' AND column2 > 100;
```

### OR
Multiple conditions are used to filter records using OR.

```
SELECT column1, column2
FROM table_name
WHERE column1 = 'value' OR column2 > 100;
```

### BETWEEN
The BETWEEN condition is used to filter records within a specified range.

```
SELECT column1, column2
FROM table_name
WHERE column1 BETWEEN 50 AND 100;
```

### LIKE
The LIKE condition is used to search for a specified pattern in a column.

#### Wildcard *%*
Used to match any sequence of characters (including zero characters).

```
SELECT column1
FROM table_name
WHERE column1 LIKE 'A%';
```

#### Wildcard *_*
Used to match a single character.

```
SELECT column1
FROM table_name
WHERE column1 LIKE 'A_';
```

### NULL
The NULL condition is used to filter records where a column has no value.

```
SELECT column1, column2
FROM table_name
WHERE column1 IS NULL;
```

### NOT NULL
Checks if a column does not have a NULL value.

```
SELECT *
FROM table_name
WHERE column_name IS NOT NULL;
```

### IN
Checks if a column's value is in a specified list.

```
SELECT *
FROM table_name
WHERE column_name IN (value1, value2, ...);
```

### NOT IN
Checks if a column's value is not in a specified list.

```
SELECT *
FROM table_name
WHERE column_name NOT IN (value1, value2, ...);
```

### CASE
Performs conditional logic within a query.

```
SELECT column1,
  CASE
    WHEN condition1 THEN 'Value1'
    WHEN condition2 THEN 'Value2'
    ELSE 'DefaultValue'
  END AS new_column
FROM table_name;
```

## AGGREGATE FUNCTIONS

### COUNT
Counts the number of rows.

```
SELECT COUNT(column)
FROM table_name;
```

### SUM
Calculates the sum of values in a column.

```
SELECT SUM(column)
FROM table_name;
```

### AVG
Calculates the average of values in a column.

```
SELECT AVG(column)
FROM table_name;
```

### MIN
Finds the minimum value in a column.

```
SELECT MIN(column)
FROM table_name;
```

### MAX
Finds the maximum value in a column.

```
SELECT MAX(column)
FROM table_name;
```

### GROUP
Groups rows that have the same values into summary rows.

```
SELECT column1, COUNT(column2)
FROM table_name
GROUP BY column1;
```

### HAVING
Filters the results of a GROUP BY clause.

```
SELECT column1, COUNT(column2)
FROM table_name
GROUP BY column1
HAVING COUNT(column2) > 1;
```


