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
- [FUNCTIONS](#functions)
  - [LEN](#len)
  - [COALESCE](#coalesce)
  - [CAST](#cast)
  - [LEFT](#left)
  - [RIGHT](#right)
  - [CHARINDEX](#charindex)
  - [SUBSTRING](#substring)
  - [TRIM](#trim)
  - [REPLACE](#replace)
  - [REVERSE](#reverse)
  - [FORMAT](#format)
  - [LOWER](#lower)
  - [UPPER](#upper)
  - [ROUND](#round)
  - [FLOOR](#floor)
  - [CEILING](#ceiling)
  - [ISNUMERIC](#isnumeric)
- [JOINS](#joins)
  - [INNER JOIN](#inner-join)
  - [LEFT JOIN](#left-join)
  - [RIGHT JOIN](#right-join)
  - [FULL OUTER JOIN](#full-outer-join)
  - [CROSS JOIN](#cross-join)
- [DATE and TIME](#date-and-time)
  - [DATE](#date)
  - [TIME](#time)
  - [DATETIME](#datetime)
  - [CURRENT_DATE](#current_date)
  - [CURRENT_TIME](#current_time)
  - [CURRENT_TIMESTAMP](#current_timestamp)
  - [DATENAME](#datename)
  - [DATEPART](#datepart)
  - [DATEDIFF](#datediff)
  - [DATEADD](#dateadd)
  - [DATEFROMPARTS](#datefromparts)
  - [DATETIMEFROMPARTS](#datetimefromparts)
  - [CONVERT](#convert)
  - [FIRST DAY OF MONTH](#first-day-of-month)
  - [LAST DAY OF MONTH](#last-day-of-month)
- [DATA MODIFICATION](#data-modification)
  - [CREATE TABLE](#create-table)
  - [INSERT INTO](#insert-into)
  - [UPDATE](#update)
  - [ALTER TABLE](#alter)
  - [DELETE](#delete)
  - [DROP TABLE](#drop)
- [WINDOW FUNCTIONS](#ranking-functions)
  - [ROW_NUMBER](#row_number)
  - [RANK](#rank)
  - [DENSE_RANK](#dense_rank)
  - [NTILE](#ntile)
  - [PARTITION BY](#partition-by)
  - [LAG](#lag)
  - [LEAD](#lead)
  - [FIRST_VALUE](#first_value)
  - [LAST_VALUE](#last_value)

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

## FUNCTIONS

### LEN
Returns the number of characters in a string.

```
SELECT LEN(column_name) AS length
FROM table_name;
```

### COALESCE
Returns the first non-null expression in the list.

```
SELECT COALESCE(column1, column2, 'DefaultValue') AS result
FROM table_name;
```

### CAST
Converts a value from one data type to another.

```
SELECT CAST(column_name AS new_data_type) AS result
FROM table_name;
```

### LEFT
Returns a specified number of characters from the beginning of a string.

```
SELECT LEFT(column_name, 3) AS left_part
FROM table_name;
```

### RIGHT
Returns a specified number of characters from the end of a string.

```
SELECT RIGHT(column_name, 3) AS right_part
FROM table_name;
```

### CHARINDEX
Returns the starting position of a substring in a string.

```
SELECT CHARINDEX('substring', column_name) AS position
FROM table_name;
```

### SUBSTRING
Extracts a substring from a string.

```
SELECT SUBSTRING(column_name, start_position, length) AS substring
FROM table_name;
```

### TRIM
Removes leading and trailing spaces from a string.

```
SELECT TRIM(column_name) AS trimmed_value
FROM table_name;
```

### REPLACE
Replaces occurrences of a specified string with another string.

```
SELECT REPLACE(column_name, 'old_value', 'new_value') AS result
FROM table_name;
```

### REVERSE
Reverses the characters in a string.

```
SELECT REVERSE(column_name) AS reversed_value
FROM table_name;
```

### FORMAT
Formats a value with the specified format.

```
SELECT FORMAT(column_name, 'yyyy-MM-dd') AS formatted_date
FROM table_name;
```

### LOWER
Converts a string to lowercase.

```
SELECT LOWER(column_name) AS lowercase_value
FROM table_name;
```

### UPPER
Converts a string to uppercase.

```
SELECT UPPER(column_name) AS uppercase_value
FROM table_name;
```

### ROUND
Rounds a numeric value to the specified number of decimal places.

```
SELECT ROUND(column_name, 2) AS rounded_value
FROM table_name;
```

### FLOOR
Returns the largest integer less than or equal to a numeric value.

```
SELECT FLOOR(column_name) AS floored_value
FROM table_name;
```

### CEILING
Returns the smallest integer greater than or equal to a numeric value.

```
SELECT CEILING(column_name) AS ceiling_value
FROM table_name;
```

### ISNUMERIC
Checks if a value is numeric.

```
SELECT column_name
FROM table_name
WHERE ISNUMERIC(column_name) = 1;
```


## JOINS

### INNER JOIN
Returns rows that have matching values in both tables.

```
SELECT columns
FROM table1
INNER JOIN table2
ON table1.column = table2.column;
```

### LEFT JOIN
Returns all rows from the left table and matching rows from the right table.

```
SELECT columns
FROM table1
LEFT JOIN table2
ON table1.column = table2.column;
```

### RIGHT JOIN
Returns all rows from the right table and matching rows from the left table.

```
SELECT columns
FROM table1
RIGHT JOIN table2
ON table1.column = table2.column;
```

### FULL OUTER JOIN
Returns all rows when there is a match in either the left or right table.

```
SELECT columns
FROM table1
FULL OUTER JOIN table2
ON table1.column = table2.column;
```

### CROSS JOIN
Combines each row from the first table with every row from the second table, resulting in a Cartesian product.

```
SELECT column1, column2
FROM table1
CROSS JOIN table2;
```

## DATE and TIME

### DATE
Represents a date, usually *YYYY-MM-DD*... but it can have other formats depending on the server.

```
SELECT DATE '2024-02-02' AS example_date;
```

### TIME
Represents a time (HH:MM:SS).

```
SELECT TIME '12:30:00' AS example_time;
```

### DATETIME
Represents a combination of date and time.

```
SELECT DATETIME '2024-02-02 12:30:00' AS example_datetime;
```

### CURRENT_DATE
Returns the current date.

```
SELECT CURRENT_DATE AS today;
```

### CURRENT_TIME
Returns the current time.

```
SELECT CURRENT_TIME AS current_time;
```

### CURRENT_TIMESTAMP
Returns the current date and time.

```
SELECT CURRENT_TIMESTAMP AS current_datetime;
```

### DATENAME
Returns a specified part of a datetime.

```
SELECT DATENAME(MONTH, '2024-02-02') AS month_name;
```

```
SELECT DATENAME(WEEKDAY, '2024-02-02') AS month_name;
```

### DATEPART
Extracts parts of a datetime value.

```
SELECT DATEPART(YEAR, '2024-02-02') AS year,
       DATEPART(MONTH, '2024-02-02') AS month,
       DATEPART(DAY, '2024-02-02') AS day;
```

### DATEDIFF
Calculates the difference between two dates.

```
SELECT DATEDIFF(DAY, '2024-02-01', '2024-02-05') AS days_difference;
```

### DATEADD
Adds or subtracts a specified time interval to a date.

```
SELECT DATEADD(MONTH, 1, '2024-02-02') AS one_month_later;
```

### DATEFROMPARTS
Creates a date from individual parts.

```
SELECT DATEFROMPARTS(2024, 2, 2) AS custom_date;
```

### DATETIMEFROMPARTS
Creates a datetime from individual parts.

```
SELECT DATETIMEFROMPARTS(2024, 2, 2, 12, 30, 0, 0) AS custom_datetime;
```

### CONVERT
Converts a string to a date.

```
SELECT CONVERT(DATE, '2024-02-02', 23) AS converted_date;
```

### FIRST_DAY_OF_MONTH
Returns the first day of the month.

```
SELECT DATEADD(MONTH, DATEDIFF(MONTH, 0, '2024-02-02'), 0) AS first_day_of_month;
```

### LAST_DAY_OF_MONTH
Returns the last day of the month.

```
SELECT EOMONTH('2024-02-02') AS last_day_of_month;
```

## DATA MODIFICATION

### CREATE TABLE
Creates a new table with specified columns and data types.

```
CREATE TABLE table_name (
  column1 datatype,
  column2 datatype,
  ...
);
```

### INSERT INTO
Adds new records to a table.

```
INSERT INTO table_name (column1, column2, ...)
VALUES (value1, value2, ...);
```

### UPDATE
Modifies existing records in a table.

```
UPDATE table_name
SET column1 = value1, column2 = value2
WHERE condition;
```

### ALTER TABLE
Modifies an existing table (e.g., add, modify, rename or drop columns).

#### Add Column
```
ALTER TABLE table_name
ADD column_name datatype;
```

#### Modify Column
```
ALTER TABLE table_name
MODIFY column_name new_datatype;
```

#### Rename Column
```
ALTER TABLE table_name
RENAME COLUMN old_column_name TO new_column_name;
```

#### Drop Column
```
ALTER TABLE table_name
DROP COLUMN column_name;
```

### DELETE
Removes records from a table.

```
DELETE FROM table_name
WHERE condition;
```

### DROP TABLE
Removes an entire table from the database.

```
DROP TABLE table_name;
```

## WINDOW FUNCTIONS

### ROW_NUMBER
Assigns a unique integer to each row within a partition of the result set, starting from 1.

```
SELECT column1, column2, ..., ROW_NUMBER() OVER (ORDER BY column1) AS row_num
FROM table_name;
```

### RANK
Assigns a unique rank to each distinct row, with ties receiving the same rank, leaving gaps between ranks.

```
SELECT column1, column2, ..., RANK() OVER (ORDER BY column1) AS ranking
FROM table_name;
```

### DENSE_RANK
Assigns a unique rank to each distinct row, with ties receiving the same rank, without leaving gaps between ranks.

```
SELECT column1, column2, ..., DENSE_RANK() OVER (ORDER BY column1) AS dense_rank
FROM table_name;
```

### NTILE
Divides the result set into a specified number of roughly equal parts, assigning a bucket number to each row.

```
SELECT column1, column2, ..., NTILE(4) OVER (ORDER BY column1) AS quartile
FROM table_name;
```

### PARTITION BY
Divides the result set into partitions to perform window functions independently on each partition.

```
SELECT column1, column2, ..., ROW_NUMBER() OVER (PARTITION BY column3 ORDER BY column1) AS row_num
FROM table_name;
```

### LAG
Accesses data from a previous row within the result set based on the specified column order.

```
SELECT column1, column2, ..., LAG(column1, 1) OVER (ORDER BY column1) AS prev_value
FROM table_name;
```

### LEAD
Accesses data from a subsequent row within the result set based on the specified column order.

```
SELECT column1, column2, ..., LEAD(column1, 1) OVER (ORDER BY column1) AS next_value
FROM table_name;
```

### FIRST_VALUE
Returns the value of the specified expression for the first row in the window frame.

```
SELECT column1, column2, ..., FIRST_VALUE(column1) OVER (ORDER BY column1) AS first_value
FROM table_name;
```

### LAST_VALUE
Returns the value of the specified expression for the last row in the window frame.

```
SELECT column1, column2, ..., LAST_VALUE(column1) OVER (ORDER BY column1) AS last_value
FROM table_name;
```
