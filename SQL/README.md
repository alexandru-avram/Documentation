# SQL Cheat Sheet

## Table of Contents
- [SELECT](#select)
  - [Basic SELECT](#basic-select)
  - [DISTINCT](#distinct)
  - [WHERE](#where)
  - [ORDER BY](#order-by)
  - [LIMIT](#limit)
- [JOINS](#joins)
  - [INNER JOIN](#inner-join)
  - [LEFT JOIN](#left-join)
  - [RIGHT JOIN](#right-join)
  - [FULL OUTER JOIN](#full-outer-join)
- [AGGREGATE FUNCTIONS](#aggregate-functions)
  - [COUNT](#count)
  - [SUM](#sum)
  - [AVG](#avg)
  - [MIN](#min)
  - [MAX](#max)
- [GROUP BY](#group-by)
- [HAVING](#having)
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
