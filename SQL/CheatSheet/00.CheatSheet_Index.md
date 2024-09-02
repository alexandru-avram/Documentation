# SQL Cheat Sheet
This is a generalized list of SQL functions that are common accross most standardized platforms.

## Table of Contents
- [SELECT](#select)
  - [BASIC SELECT](#basic-select)
  - [DISTINCT](#distinct)
  - [ORDER BY](#order-by)
  - [LIMIT](#limit)
  - [FETCH and OFFSET](#fetch-and-offset)
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
  - [CONCAT](#concat)
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
  - [SCALAR SUBQUERY](#scalar-subquery)
  - [CORRELATED SUBQUERY](#correlated-subquery)
  - [SUBQUERY IN DERIVED TABLE](#subquery-in-derived-table)
  - [SUBQUERY IN SELECT CLAUSE](#subquery-in-select-clause)
- [CONTROL FLOW](#control-flow)
  - [IF-ELSE](#if-else)
  - [WHILE](#while)
  - [FOR](#for)
  - [GOTO](#goto)
- [VIEWS](#views)
  - [CREATE VIEW](#create-view)
  - [SELECT FROM VIEW](#select-view)
  - [ALTER VIEW](#alter-view)
  - [DROP VIEW](#drop-view)
- [STORED PROCEDURES AND FUNCTIONS](#stored-procedures-and-functions)
  - [USER-DEFINED FUNCTIONS (UDFs)](#user-defined-functions-udfs)
  - [STORED PROCEDURES](#stored-procedures)
  - [INLINE TABLE-VALUED FUNCTIONS](#inline-table-valued-functions)
  - [COMMON TABLE EXPRESSIONS (CTEs)](#common-table-expressions-ctes)
  - [TRIGGERS](#triggers)
- [TRANSACTIONS](#transactions)
  - [BEGIN TRANSACTION](#begin-transaction)
  - [COMMIT](#commit)
  - [ROLLBACK](#rollback)
- [USER-DEFINED DATA TYPE](#user-defined-data-type)
  - [CREATE DOMAIN](#create-domain)
  - [CREATE TYPE](#create-type)
  - [DROP DOMAIN](#drop-domain)
- [DATABASE CONSTRAINTS AND KEYS](#database-constraints-and-keys)
  - [PRIMARY KEY](#primary-key)
  - [FOREIGN KEY](#foreign-key)
  - [UNIQUE](#unique)
  - [CHECK](#check)
  - [CONSTRAINT](#constraint)
- [SEQUENCE](#sequence)
  - [CREATE SEQUENCE](#create-sequqnce)
  - [GENERATING VALUES](#generating-values)
  - [CURRENT VALUE](#current-value)
  - [SET VALUE](#set-value)
  - [ALTER SEQUENCE](#alter-sequence)
  - [RESTARTING A SEQUENCE](#restarting-a-sequence)
  - [DESCENDING SEQUENCE](#descending-sequence)
  - [CYCLE](#cycle)
  - [INSERTING A SEQUENCE](#inserting-a-sequence)
    
---

## SELECT

### BASIC SELECT
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

### FETCH and OFFSET
The *FETCH* statement in SQL is used in combination with the *ORDER BY* clause to retrieve a specified number of rows from the result set of a query. It is commonly used in scenarios where you want to paginate through a large result set, fetching a subset of rows at a time. The *FETCH* statement is often used in conjunction with *OFFSET* to skip a certain number of rows before retrieving the specified number of rows.

```
SELECT column1, column2, ...
FROM table_name
ORDER BY column1, column2, ...
OFFSET {number_of_rows_to_skip} ROWS
FETCH {number_of_rows_to_fetch} ROWS ONLY;
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
The *BETWEEN* condition is used to filter records within a specified range.

```
SELECT column1, column2
FROM table_name
WHERE column1 BETWEEN 50 AND 100;
```

The *NOT BETWEEN* condition is used to filter records outside a specified range.

```
SELECT column1, column2
FROM table_name
WHERE column1 NOT BETWEEN 50 AND 100;
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

#### ILIKE
The *ILIKE* condition is specific to some database systems, such as **PostgreSQL**. It performs a case-insensitive pattern match similar to *LIKE*. This means it will match patterns regardless of the case of the letters.

```
SELECT * FROM employees WHERE first_name ILIKE 'a%';
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

### CONCAT
Concatenates two or more strings into a single string.

```
CONCAT(string1, string2, ...)
```

#### CONCAT_WS
Stands for *concatenate with separator*. It concatenates two or more strings into a single string, but it allows you to specify a separator that is placed between the concatenated strings.

```
CONCAT_WS(separator, string1, string2, ...)
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

## SUBQUERIES
Subqueries (also known as nested queries or inner queries) in SQL are queries embedded within another query. They are enclosed within parentheses and can be used in various parts of a SQL statement where an expression is allowed. Subqueries can return a single value, a column, or a set of rows.

### SCALAR SUBQUERY
A scalar subquery returns a single value and can be used in a context where a single value is expected, such as a comparison or assignment.

```
-- Find employees whose salary is greater than the average salary in the department
SELECT employee_name
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees WHERE department_id = 101);
```

### CORRELATED SUBQUERY
A correlated subquery is a subquery that references columns from the outer query. It is evaluated once for each row processed by the outer query.

```
-- Find employees whose salary is greater than the average salary in their department
SELECT employee_name
FROM employees e1
WHERE salary > (SELECT AVG(salary) FROM employees e2 WHERE e1.department_id = e2.department_id);
```

### SUBQUERY IN DERIVED TABLE
A subquery in the FROM clause is used to create a derived table, which is then used in the main query.

```
-- Find the average salary of employees in each department
SELECT department_name, avg_salary
FROM (
    SELECT department_id, AVG(salary) as avg_salary
    FROM employees
    GROUP BY department_id
) AS department_avg;
```

### SUBQUERY IN SELECT CLAUSE
A subquery in the SELECT clause is used to retrieve a single value or a set of values to be included in the result set.

```
-- Display employee names with their corresponding department names
SELECT employee_name,
       (SELECT department_name FROM departments WHERE department_id = employees.department_id) AS department_name
FROM employees;
```

## CONTROL FLOW

### IF-ELSE
Allows for conditional execution of SQL statements.

```
IF condition
BEGIN
  -- Statements to execute if condition is true
END
ELSE
BEGIN
  -- Statements to execute if condition is false
END;
```

### WHILE
Repeats a set of SQL statements as long as the specified condition is true.

WHILE condition
BEGIN
  -- Statements to execute
END;

### FOR
SQL Server doesn't have a native FOR loop like some other languages. Instead, you can use a WHILE loop with a counter.

```
DECLARE @counter INT = 1;

WHILE @counter <= 5
BEGIN
  PRINT 'Iteration: ' + CAST(@counter AS VARCHAR(10));
  SET @counter = @counter + 1;
END;
```

### GOTO
Allows for jumping to a specified label within a batch or stored procedure. RUsing GOTO is generally discouraged as it can make code harder to read and maintain. It's often better to use structured control flow constructs like IF-ELSE or CASE when possible.

```
IF condition
  GOTO label;

-- Statements to execute if condition is false

:label
-- Statements to execute if condition is true
```

## VIEWS
A SQL view is a virtual table derived from the result of a SELECT query. Unlike physical tables, views do not store the data themselves but provide a way to represent the result of a query as a named, reusable object. Views can be used to simplify complex queries, encapsulate business logic, and provide a security layer by restricting access to specific columns or rows.

### CREATE VIEW
Creates a virtual table based on the result of a SELECT query.

```
CREATE VIEW view_name AS
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

### SELECT FROM VIEW
Retrieves data from a view using a SELECT statement.

```
SELECT column1, column2, ...
FROM view_name;
```

### ALTER VIEW
Modifies the definition of an existing view.

```
ALTER VIEW view_name AS
SELECT new_column1, new_column2, ...
FROM new_table_name
WHERE new_condition;
```

### DROP VIEW
Deletes an existing view.

```
DROP VIEW view_name;
```

## STORED PROCEDURES AND FUNCTIONS

### USER-DEFINED FUNCTIONS (UDFs)
A User-Defined Function (UDF) in SQL is a custom function created by the user to encapsulate a specific piece of logic. UDFs take parameters, perform a computation, and return a single value.

```
CREATE FUNCTION CalculateDiscount(price DECIMAL, discount_rate DECIMAL)
RETURNS DECIMAL
BEGIN
  DECLARE discounted_price DECIMAL;
  SET discounted_price = price - (price * discount_rate);
  RETURN discounted_price;
END;
```

### STORED PROCEDURES
A Stored Procedure is a precompiled collection of one or more SQL statements that can be executed as a single unit. Stored Procedures are typically used to encapsulate business logic, perform operations on the database, or execute a series of SQL statements. They can accept parameters, return values, and can be executed by other programs or scripts.

```
CREATE PROCEDURE UpdateEmployeeSalary(employee_id INT, new_salary DECIMAL)
BEGIN
  UPDATE employees
  SET salary = new_salary
  WHERE id = employee_id;
END;
```

### INLINE TABLE-VALUED FUNCTIONS
Similar to UDFs, Inline Table-Valued Functions return a table as a result. They can be used in the FROM clause of a SELECT statement, and their results can be treated like a regular table.

```
CREATE FUNCTION GetEmployeesByDepartment(@dept_id INT)
RETURNS TABLE
AS
RETURN (
  SELECT * FROM employees WHERE department_id = @dept_id
);
```

### COMMON TABLE EXPRESSIONS (CTEs)
CTEs provide a way to define temporary result sets within a SELECT, INSERT, UPDATE, or DELETE statement. They make complex queries more readable by breaking them down into smaller, named, and reusable units.

```
WITH MonthlySales AS (
  SELECT employee_id, SUM(sales_amount) AS total_sales
  FROM sales
  WHERE DATE_PART('month', sale_date) = DATE_PART('month', CURRENT_DATE)
  GROUP BY employee_id
)
SELECT * FROM MonthlySales WHERE total_sales > 10000;
```

### TRIGGERS
Triggers are powerful database objects that can automatically respond to events like INSERT, UPDATE, or DELETE on a table. They are useful for maintaining data integrity, logging changes, or enforcing business rules.

```
-- Create Trigger
CREATE TRIGGER trigger_name
AFTER INSERT OR UPDATE OR DELETE ON table_name
FOR EACH ROW
BEGIN
  -- trigger logic
END;
```

```
-- Example Trigger
DELIMITER //
CREATE TRIGGER after_insert_example
AFTER INSERT ON example_table
FOR EACH ROW
BEGIN
  INSERT INTO log_table (event_type, event_description, event_date)
  VALUES ('INSERT', CONCAT('New record added with ID: ', NEW.id), NOW());
END;
//

-- Drop Trigger
DROP TRIGGER IF EXISTS trigger_name;
```

In the example trigger above, a trigger named after_insert_example is created. It fires after each INSERT operation on the example_table. It logs the event into a log_table with details about the inserted record.


## TRANSACTIONS
Transactions in the context of databases refer to a set of one or more SQL statements that are executed as a single unit of work. The concept of transactions ensures that database operations are atomic, consistent, isolated, and durable, commonly known as the ACID properties.

### BEGIN TRANSACTION
Starts a new transaction. All subsequent SQL statements are part of this transaction until it is explicitly committed or rolled back.

```
BEGIN TRANSACTION;
```

### COMMIT
Saves all the changes made during the current transaction to the database. This makes the changes permanent.

```
COMMIT;
```

### ROLEBACK
Undoes all the changes made during the current transaction. It returns the database to its state before the transaction began.

```
ROLLBACK;
```

**Full example**

```
-- Start a new transaction
BEGIN TRANSACTION;

-- SQL statements within the transaction
UPDATE Accounts SET balance = balance - 100 WHERE account_id = 123;  -- Valid update
-- Simulate an error by attempting to update a non-existing account
UPDATE Accounts SET balance = balance - 100 WHERE account_id = 999;  -- Error: Account does not exist

-- Check for errors and decide whether to commit or roll back
IF @@ERROR <> 0
BEGIN
    -- An error occurred, roll back the entire transaction
    ROLLBACK;
    PRINT 'Transaction rolled back due to an error.';
END
ELSE
BEGIN
    -- No error occurred, commit the transaction, making the changes permanent
    COMMIT;
    PRINT 'Transaction committed successfully.';
END;
```

## USER-DEFINED DATA TYPES

### CREATE DOMAIN
`CREATE DOMAIN` allows you to define a new data type with optional constraints. It's useful when you need to ensure consistency and enforce rules for a specific type of data across multiple columns or tables.

```
CREATE DOMAIN domain_name AS data_type [DEFAULT default_value] [CHECK constraint];
```

**Example (email address)**

```
CREATE DOMAIN EmailAddress VARCHAR(255) NOT NULL
CHECK (VALUE LIKE '%@%.%');
```

**Example ENUM or SET values**

```
CREATE DOMAIN colors VARCHAR(30) NOT NULL
CHECK (VALUE IN ('red', 'blue', 'yellow'));
```

### CREATE TYPE
`CREATE TYPE` enables you to define a new composite type or custom data type in PostgreSQL. It's handy when you want to bundle together multiple fields under a single data type, especially if you intend to reuse that structure across tables or queries.

```
CREATE TYPE type_name AS (attribute1 data_type, attribute2 data_type, ...);
```

**Example full address**
```
CREATE TYPE AddressType AS (
  street_address VARCHAR(255),
  city VARCHAR(100),
  state CHAR(2),
  zip_code VARCHAR(10)
);
```

### DROP DOMAIN
Delete a custom domain created on the schema.

```
DROP DOMAIN domain_name
```

If the domain is used, it will not be deleted unless you use `CASCADE`. However, unless you want to loose the data on the columns using a custom domain-type, ensure you ALTER the data type on the columns.

```
DROP DOMAIN domain_name CASCADE
```

## DATABASE CONSTRAINTS AND KEYS

### PRIMARY KEY
A primary key is a column or a set of columns that uniquely identifies each row in a table. It enforces entity integrity, meaning each row in a table is uniquely identified and cannot contain null values.

```
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50)
);
```
### FOREIGN KEY
A foreign key is a column or a set of columns in a table that establishes a link between data in two tables. It enforces referential integrity, ensuring that the values in the foreign key column(s) match the values in the primary key of another table.

```
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);
```

### UNIQUE
A unique constraint ensures that the values in a column or a set of columns are unique across all rows in a table. Unlike primary keys, unique constraints allow null values unless specified otherwise.

```
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(50) UNIQUE,
    date_of_birth DATE
);
```

### CHECK
A check constraint defines a condition that each row in a table must satisfy. It ensures that the values in a column meet specific criteria, preventing invalid data from being inserted into the table.

```
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    price DECIMAL(10, 2),
    quantity INT,
    CHECK (price > 0 AND quantity >= 0)
);
```

### CONSTRAINT
A constraint is a rule defined on a column or a set of columns in a table that restricts the values allowed in those columns. It can be used to enforce data integrity and maintain consistency in the database.

```
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    CONSTRAINT chk_employee_age CHECK (age >= 18)
);
```

## SEQUENCE
`SEQUENCE` is a database object that is used to generate a sequence of unique numeric values, typically used for auto-incrementing primary keys or other unique identifiers in a table. Sequences are useful for generating unique identifiers independently of any table, making them more flexible than auto-increment columns.

### CREATE SEQUENCE

You can create a sequence using the `CREATE SEQUENCE` statement. When creating a sequence, you can specify various options such as the starting value, increment value, minimum value, maximum value, and whether the sequence should cycle when it reaches its maximum or minimum value.

```
CREATE SEQUENCE IF NOT EXISTS sequence_name as INT
START WITH start_value
INCREMENT BY increment_value
MINVALUE min_value
MAXVALUE max_value;
```

### GENERATING VALUES
Once a sequence is created, you can generate the next value in the sequence using the `NEXTVAL` function.

```
SELECT NEXTVAL('sequence_name');
```

### CURRENT VALUE
The current value of the sequence can be obtained using the `CURRVAL` function, but `CURRVAL` can only be used after `NEXTVAL` has been called at least once in the session.

```
SELECT CURRVAL('sequence_name');
```

### SET VALUE
You can also set the current value of the sequence using `SETVAL`.

```
SELECT SETVAL('sequence_name', 100);
```

In order to set a new value, without skipping, add a `false` at the end.


```
SELECT SETVAL('sequence_name', 100, false);
```

### ALTER SEQUENCE
You can modify an existing sequence using `ALTER SEQUENCE`.

```
ALTER SEQUENCE sequence_name INCREMENT BY 5;
```


### RESTARTING A SEQUENCE
To restart a sequence, use `ALTER` in combination with `RESTART`

```
ALTER SEQUENCE sequence_name RESTART WITH 100;
```

### DESCENDING SEQUENCE
By incrementing the sequence with -1, you can also create descending sequences.

```
CREATE SEQUENCE IF NOT EXISTS sequence_name as INT
START WITH 100
INCREMENT BY -1
```

### CYCLE
When creating a sequence, you can also use `CYCLE` in order to cycle the sequence when it's needed. The default is `NO CYCLE`.

```
CREATE SEQUENCE IF NOT EXISTS sequence_name as INT
START WITH start_value
INCREMENT BY increment_value
MINVALUE min_value
MAXVALUE max_value
CYCLE;
```

### INSERTING A SEQUENCE
Sequences are most useful when used to inster into a table.

```
CREATE TABLE table_name (
    id SERIAL PRIMARY KEY,
    column1 VARCHAR2(50) NOT NULL,
    column2 VARCHAR2(100) NOT NULL
);


INSERT INTO table (id, column1, column2)
VALUES (user_id_seq.NEXTVAL, 'value_column1', 'vaolue_column2');
```
