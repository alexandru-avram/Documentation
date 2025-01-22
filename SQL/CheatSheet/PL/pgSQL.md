# PL/pgSQL

- [BASIC SYNTAX and STRUCTURE](#Basic-Syntax-and-Structure)
  - [Block Structure](#block-structure)
  - [Anonymous Blocks](#Anonymous-Blocks)
  - [Named Blocks](#Named-Blocks)
  - [Statements](#Statements)
    - [RAISE](#raise)
    - [RETURN](#return)
    - [PERFORM](#perform)
    - [EXECUTE](#execute)
    - [RETURN QUERY](#return-query)
    - [ASSERT](#assert)
    - [LOOP and EXIT](#loop-and-exit)
- [VARIABLES](#variables)
  - [ALIAS](#alias)
  - [Assigning Values to Variables](#Assigning-Values-to-Variables)
  - [Type Casting and Conversion](#Type-Casting-and-Conversion)
  - [VARIABLE SCOPE](#variable-scope)
  - [Compound Data Types](#Compound-Data-Types)
  - [IN OUT INOUT](#IN-OUT-INOUT)
- [Control Flow Structures](#control-flow-structures)
  - [Conditional Statements](#conditional-statements)
  - [CASE Statement](#case-statement)
  - [LOOP Strcutures](#loop-structures)


## BASIC SYNTAX and STRUCTURE

### Block Structure
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

### Anonymous Blocks
In order to create temporary, anonymous and unnamed blocks, use `DO`:

```
DO
$$
  BEGIN
  END
$$;
```

### Named Blocks
More complex structures, which are stored in the DB, use a `CREATE OR REPLACE` statement in the beggining.

```
CREATE OR REPLACE FUNCTION function_name (parameters datatypes)
RETURNS return_datatype AS
$$
DECLARE
BEGIN
  RETURN return_value;
END;
```

### Statements
#### RAISE
`RAISE` is used to display messages or raise exceptions with PL/pgSQL code.

```
BEGIN
  RAISE NOTICE 'This is a notice message';
  RAISE WARNING 'This is a warning message';
  RAISE EXCEPTION 'This is an exception';
END;
```

#### RETURN
`RETURN` is used to return a value from a function.
* `RETURN <expression>` to exit and return a value
* `RETURN NEXT` and `RETURN QUERY` for functions that return sets.

```
CREATE FUNCTION double_number (num INT)
RETURNS INT AS
$$
BEGIN
  RETURN num * 2;
END;
```

#### PERFORM
`PERFORM` exectues a command without expecting a result. It's useful for calling functions that don't return a value. Often used for procedures where only the side effects are needed and not the return value.

Example: `log_user_activity` might be a function that logs a user's actions to an audit table, but doesn't return any value that the calling code needs.
```
PERFORM log_user_activity(user_id, `login`);
```


#### EXECUTE
`EXECUTE` executes a dynamically created SQL statement. It's primarily used when building queries dynamically. To be used carefully, as it can lead to SQL injection.

```
EXECUTE 'SELECT * FROM' || table_name;
```

#### RETURN QUERY
Returns a set of results from a function for functions that return sets. Useful for functions that need to return a full results set instead of a single value.

```
RETURN QUERY SELECT * FROM my_table WHERE condition;
```

#### ASSERT
Used to validate assumtpions in code and raising an error if conditions are not met. Very useful when debugging.

```
ASSERT condition, 'Error message if condition fails';
```

#### LOOP and EXIT
They are used to create and end loops with PL/pgSQL.

```
LOOP
  -- loop code here
  EXIT WHEN condition;
END LOOP;
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

### ALIAS
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


### Assigning Values to Variables
You can use `:=` to directly assign values to variables. If you put them in the `DECLARE` structure, that is the DEFAULT value for the variable.

```
DECLARE
  flag TEXT := 'Y';
```


Assign the result of a query to a variable using the `SELECT INTO` statement.

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
    row_employee RECORD;
  BEGIN
    SELECT * FROM employees
    INTO row_employee
    WHERE employee_id = 1;

    RAISE NOTICE 'Your employee is %, row_employee.employee_name
  END;
$$
```

### Type Casting and Conversion
Use the `::` operator or the `CAST` function to change the data types.

```
DECLARE
  num_value INT := 42;
  text_value TEXT;
BEGIN
  text_value := num_value::TEXT;
  text_value := CAST(num_value as TEXT);
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

### IN OUT INOUT
In PL/pgSQL, `IN` and `OUT` parameters are used primarily in functions and procedures to control how parameters are passed and returned. They define whether a parameter is for input only, output only, or both (using `INOUT`).

#### IN Parameters
They pass data into the function or procedure. These parameters are read-only and cannot be modified within the function or procedure. Parameters in PL/pgSQL are `IN` by default, so if you don’t specify `IN`, PostgreSQL will assume it.

```
CREATE OR REPLACE FUNCTION get_employee_salary(emp_id INTEGER)
RETURNS NUMERIC AS $$
DECLARE
    emp_salary NUMERIC;
BEGIN
    SELECT salary INTO emp_salary FROM employees WHERE id = emp_id;
    RETURN emp_salary;
END;
$$ LANGUAGE plpgsql;
```

#### OUT Parameters
Defines an output parameter that will hold the result to be returned to the caller. `OUT` parameters act as variables initialized to NULL and can be assigned values within the function or procedure.

```
CREATE OR REPLACE FUNCTION get_employee_details(emp_id INTEGER, OUT emp_name VARCHAR, OUT emp_salary NUMERIC)
AS $$
BEGIN
    SELECT name, salary INTO emp_name, emp_salary FROM employees WHERE id = emp_id;
END;
$$ LANGUAGE plpgsql;

-- Calling an OUT Function: The function automatically returns the values of emp_name and emp_salary.

SELECT * FROM get_employee_details(1);
```

#### INOUT Parameters
Use `INOUT` parameters when you need a parameter to serve both as an input and output. The caller provides an initial value, and the function can modify and return it.

```
CREATE OR REPLACE FUNCTION update_salary(emp_id INTEGER, INOUT emp_salary NUMERIC)
AS $$
BEGIN
    UPDATE employees SET salary = emp_salary WHERE id = emp_id;
    SELECT salary INTO emp_salary FROM employees WHERE id = emp_id;  -- Updated value
END;
$$ LANGUAGE plpgsql;
```

Example: This is a function that performs two calculations and returns the value.

```
CREATE OR REPLACE FUNCTION fn_my_sum_2_par1(IN x int, IN y int, OUT w int, OUT z int) AS
$$
	BEGIN

		z := x + y;
		w := x * y;

	END;
$$
LANGUAGE PLPGSQL;

SELECT * FROM fn_my_sum_2_par1(1,2);
```

## Control Flow Structures

### Conditional statements

The `IF-ELSE` statement is used to execute code conditionally based on Boolean expressions.

```
IF condition THEN
    -- Code to execute if condition is true
ELSIF another_condition THEN
    -- Code to execute if the previous condition is false and this condition is true
ELSE
    -- Code to execute if none of the above conditions are true
END IF;
```

Example with a table:

```
DO $$
DECLARE
    emp RECORD;
BEGIN
    FOR emp IN SELECT * FROM employees LOOP
        IF emp.salary > 50000 THEN
            UPDATE employees
            SET status = 'Senior'
            WHERE id = emp.id;
            RAISE NOTICE 'Updated % to Senior status', emp.name;
        ELSE
            UPDATE employees
            SET status = 'Junior'
            WHERE id = emp.id;
            RAISE NOTICE 'Updated % to Junior status', emp.name;
        END IF;
    END LOOP;
END $$;

```

### CASE Statement

The `CASE` statement is similar to the `IF-ELSE` structure but is often more concise and easier to read when dealing with multiple conditions.

#### Simple CASE
The simple `CASE` evaluates a single expression and matches it against multiple values.

```
CASE expression
    WHEN value1 THEN
        -- Code if expression equals value1
    WHEN value2 THEN
        -- Code if expression equals value2
    ELSE
        -- Code if no match is found
END CASE;
```

#### Searched CASE
The searched `CASE` evaluates multiple Boolean expressions, similar to an `IF-ELSE` structure.  While the simple `CASE` is used when you want to compare a single variable or expression to multiple possible values, the search `CASE` allows more flexible conditions that don't have to reference the same expression. Istead, it can evalue entirely different conditions for each `WHEN`.

```
CASE
    WHEN var < condition1 THEN
        -- Code if condition1 is true
    WHEN var BETWEEN condition1 and condition2  THEN
        -- Code if condition2 is true
    WHEN var > condition3 THEN
        -- Code if condition2 is true  
    ELSE
        -- Code if none of the conditions are true
END CASE;
```

### LOOP Structures
The basic `LOOP` construct repeats a block of code indefinitely until an `EXIT` statement is encountered.

```
LOOP
    -- Code to repeat
    EXIT WHEN condition;
END LOOP;
```

#### FOR Loop
The `FOR` loop is commonly used for iterating over a range of numbers or the results of a query.

```
FOR counter IN start_value..end_value LOOP
    -- Code to execute
END LOOP;
```

```
BEGIN
    FOR i IN 1..5 LOOP
        RAISE NOTICE 'i: %', i;
    END LOOP;
END;
```

The `FOR` loop can also iterate over each row returned by a query.

```
FOR record IN SELECT * FROM employees LOOP
    -- Use record.field_name to access column data
END LOOP;
```

```
BEGIN
    FOR emp IN SELECT name, salary FROM employees LOOP
        RAISE NOTICE 'Employee: %, Salary: %', emp.name, emp.salary;
    END LOOP;
END;
```

#### WHILE Loop
The `WHILE` loop repeats a block of code as long as a specified condition remains true.

```
WHILE condition LOOP
    -- Code to execute
END LOOP;
```

```
DECLARE
    counter INTEGER := 1;
BEGIN
    WHILE counter <= 5 LOOP
        RAISE NOTICE 'Counter: %', counter;
        counter := counter + 1;
    END LOOP;
END;
```


#### FOREACH Loop
The `FOREACH` loop iterates over elements of an array. This is useful for operations on each element in a collection.

```
DECLARE
    num_array INTEGER[] := ARRAY[1, 2, 3, 4, 5];
BEGIN
    FOREACH num IN ARRAY num_array LOOP
        RAISE NOTICE 'Number: %', num;
    END LOOP;
END;
```

#### CONTINUE and EXIT Statements

- **EXIT**: Used to exit a loop when a specific condition is met.
- **CONTINUE**: Skips the current iteration and continues with the next iteration of the loop.

```
DECLARE
    i INTEGER;
BEGIN
    FOR i IN 1..10 LOOP
        IF i = 3 THEN
            CONTINUE;  -- Skips the current iteration when i = 3
        END IF;
        IF i = 8 THEN
            EXIT;  -- Exits the loop when i = 8
        END IF;
        RAISE NOTICE 'Value of i: %', i;
    END LOOP;
END;
```
