This sheet contains PL/SQL elements found in other sheets:

- [CONTROL FLOW](https://github.com/alexandruavram-rusu/Documentation/blob/main/SQL/CheatSheet/08.%20Control%20Flow.md)
- [USER DEFINED ELEMENTS](https://github.com/alexandruavram-rusu/Documentation/blob/main/SQL/CheatSheet/09.%20User%20Defined%20Elements.md)
<br>

- [PL/SQL](PL/SQL)
- [PL/pgSQL](PL/pgSQL)
- [PL/Python](PL/Python)

<br>

# PL/pgSQL

Every PL/pgSQL program consists of three sections in order to form a block:

- **Declaration**: Declare variables, constants, and cursors.
- **Execution**: Contains the SQL and PL/SQL statements.
- **Exception Handling**: Handles exceptions and errors.

```
<<label>>  -- Optional label for the block
DECLARE
    -- Declaration section
    variable_name datatype;
BEGIN
    -- Execution section
    -- SQL or PL/SQL statements
EXCEPTION
    -- Exception section
    WHEN exception_name THEN
        -- error handling
END;
language PLPGSQL;
```


## VARIABLES

A variable holds a value that can be changed throught the block, while a constant can only have one value that cannot be changed. Before using one or the other, they mush be declared in the declaration section.

```
DECLARE

  variable_name datatype := initial_value;
  constant_name CONSTANT datatype := constant_value;
...
BEGIN
  ...
END;
```



### ALIAS and %TYPE and %ROWTYPE

You can also use an `ALIAS FOR` to declare variables as well.

```
CREATE OR REPLACE FUNCTION function_name (int, int) RETURNS int AS
$$
...
  DECLARE
    x ALIAS FOR $1;
    y ALIAS FOR $2;
  BEGIN
    ...
  END;
$$
LANGUAGE plpgsql
```

**%TYPE**: Declares a variable with the same type as a column or another variable. Useful for keeping the data type consistent with table structure.

```
DECLARE
    emp_id employees.id%TYPE;  -- Same type as employees.id
BEGIN
    SELECT id INTO emp_id FROM employees LIMIT 1;
```

**%ROWTYPE**: Declares a variable representing an entire row of a table or query result.

```
DECLARE
    emp_record employees%ROWTYPE;
BEGIN
    SELECT * INTO emp_record FROM employees WHERE id = 1;
    RAISE NOTICE 'Employee Name: %', emp_record.name;
```


### SELECT INTO
Assign the result of a query to a variable.

```
DECLARE
    emp_salary NUMERIC;
BEGIN
    SELECT salary INTO emp_salary FROM employees WHERE id = 1;
```

You can also use `RECORD` to get the full result of a table in a variable.

```
DO
$$
  DECLARE
    row_employee record;
  BEGIN
    SELECT * FROM employees
    INTO row_employee
    WHERE employee_id = 1;

    RAISE NOTICE 'Your employee is %, row_employee.employee_name
  END;
$$
```

### VARIABLE SCOPE
Variables declared in a `DECLARE` section are only accessible within the specific block or function. Variables declared in an inner block can shadow (hide) variables of the same name in an outer block.

```
DECLARE
    count INTEGER := 5;
BEGIN
    DECLARE
        count INTEGER := 10;  -- Shadows the outer `count` variable
    BEGIN
        RAISE NOTICE 'Inner count: %', count;  -- Prints 10
    END;
    RAISE NOTICE 'Outer count: %', count;      -- Prints 5
END;
```


### Compound Data Types

**Arrays**: PL/pgSQL allows array variables to hold multiple values of the same data type.

```
DECLARE
    num_array INTEGER[] := ARRAY[1, 2, 3, 4];
BEGIN
    RAISE NOTICE 'Second element: %', num_array[2];
END;
```

**Record Type**: PL/pgSQL allows for variables to hold custom row types defined as records. Use this when querying tables with unknown structures or dynamic result sets.

```
DECLARE
    result RECORD;
BEGIN
    FOR result IN SELECT * FROM employees LOOP
        RAISE NOTICE 'Employee Name: %', result.name;
    END LOOP;
```
