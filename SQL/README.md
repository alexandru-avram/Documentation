# SQL Cheat Sheet

## Table of Contents

1. [SELECT Statement](#select-statement)
2. [FROM Clause](#from-clause)
3. [WHERE Clause](#where-clause)
4. [ORDER BY Clause](#order-by-clause)
5. [LIMIT Clause](#limit-clause)
6. [OFFSET Clause](#offset-clause)
7. [INSERT Statement](#insert-statement)
8. [UPDATE Statement](#update-statement)
9. [DELETE Statement](#delete-statement)
10. [GROUP BY Clause](#group-by-clause)
11. [HAVING Clause](#having-clause)
12. [JOIN Clause](#join-clause)
13. [INNER JOIN](#inner-join)
14. [LEFT JOIN](#left-join)
15. [RIGHT JOIN](#right-join)
16. [FULL JOIN](#full-join)
17. [UNION Operator](#union-operator)
18. [CREATE TABLE Statement](#create-table-statement)
19. [ALTER TABLE Statement](#alter-table-statement)
20. [DROP TABLE Statement](#drop-table-statement)
21. [CREATE INDEX Statement](#create-index-statement)
22. [UNIQUE Constraint](#unique-constraint)
23. [PRIMARY KEY Constraint](#primary-key-constraint)
24. [FOREIGN KEY Constraint](#foreign-key-constraint)
25. [CHECK Constraint](#check-constraint)
26. [Aggregate Functions](#aggregate-functions)
27. [Subqueries](#subqueries)
28. [CASE Statement](#case-statement)

## SELECT Statement

The `SELECT` statement is used to query the database and retrieve data from one or more tables.

```sql
SELECT column1, column2
FROM table_name
WHERE condition;
