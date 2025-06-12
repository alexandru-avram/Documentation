# Cursors

A cursor is a pointer (or a handle) to a memory area called the context area where Oracle processes SQL statements and stores the result set. You often want to process rows one at a time, using logic (IFs, calculations, logging, etc.) That’s where cursors come in — they allow row-by-row iteration over query results

Think of a cursor like a bookmark or a pointer that helps you:
 - Access the rows of a SQL query one by one
 - Keep track of the current position
 - Control how data is fetched, processed, or looped over

## Type of Cursors

There are two main types of cursors

| Cursor Type         | Description                            | Use Case                        |
| ------------------- | -------------------------------------- | ------------------------------- |
| **Implicit Cursor** | Auto-created for single-row DML/SELECT | Simple, one-time use            |
| **Explicit Cursor** | Declared and controlled manually       | Multi-row queries, more control |

### Implicit Cursors
Oracle automatically creates them for you when you run a `SELECT INTO`, `INSERT`, `UPDATE`, or `DELETE`.

```
DECLARE
  v_name employees.name%TYPE;
BEGIN
  SELECT name INTO v_name FROM employees WHERE id = 101;
  DBMS_OUTPUT.PUT_LINE('Name: ' || v_name);
END;
```

Status Info (with `%` attributes):
- `SQL%ROWCOUNT` – how many rows affected
- `SQL%FOUND` – TRUE if at least one row affected
- `SQL%NOTFOUND` – TRUE if no rows affected
- `SQL%ISOPEN` – always FALSE for implicit cursors

### Explicit Cursors
You declare the cursor yourself and control:
- Declaring
- Opening
- Fetching
- Closing

```
DECLARE
  CURSOR emp_cur IS
    SELECT id, name FROM employees;

  v_id employees.id%TYPE;
  v_name employees.name%TYPE;
BEGIN
  OPEN emp_cur;
  LOOP
    FETCH emp_cur INTO v_id, v_name;
    EXIT WHEN emp_cur%NOTFOUND;

    DBMS_OUTPUT.PUT_LINE('[' || v_id || '] ' || v_name);
  END LOOP;
  CLOSE emp_cur;
END;
```


## Curosr Lifecycle

| Step    | Description                                        |
| ------- | -------------------------------------------------- |
| Declare | Define the query and create the cursor             |
| Open    | Run the query and populate the result set          |
| Fetch   | Retrieve the current row into variables or records |
| Close   | Release the memory/resources used by the cursor    |

## Cursor Attributes

| Attribute   | Description                                 |
| ----------- | ------------------------------------------- |
| `%ISOPEN`   | TRUE if the cursor is currently open        |
| `%FOUND`    | TRUE if the last fetch returned a row       |
| `%NOTFOUND` | TRUE if the last fetch did NOT return a row |
| `%ROWCOUNT` | Number of rows fetched so far               |

```
DECLARE
  -- Declare a cursor to fetch employee ID and name from a specific department
  CURSOR emp_cur IS
    SELECT id, name FROM employees WHERE department_id = 10;

  -- Declare variables to hold fetched values
  v_id   employees.id%TYPE;
  v_name employees.name%TYPE;

BEGIN
  -- Check if the cursor is open before using it (should be FALSE initially)
  IF emp_cur%ISOPEN THEN
    DBMS_OUTPUT.PUT_LINE('Cursor is unexpectedly already open!');
  ELSE
    DBMS_OUTPUT.PUT_LINE('Cursor is initially closed.');
  END IF;

  -- Open the cursor manually
  OPEN emp_cur;

  -- After opening, ISOPEN should now return TRUE
  IF emp_cur%ISOPEN THEN
    DBMS_OUTPUT.PUT_LINE('Cursor is now open.');
  END IF;

  -- Loop through the cursor manually using FETCH
  LOOP
    FETCH emp_cur INTO v_id, v_name;

    -- Check if a row was fetched (opposite of %NOTFOUND)
    IF emp_cur%FOUND THEN
      -- Print the current row's values
      DBMS_OUTPUT.PUT_LINE('Row ' || emp_cur%ROWCOUNT || ': ' || v_id || ' - ' || v_name);
    ELSE
      -- Exit the loop if no more rows
      EXIT;
    END IF;
  END LOOP;

  -- Close the cursor
  CLOSE emp_cur;

  -- Final confirmation that cursor is closed
  IF NOT emp_cur%ISOPEN THEN
    DBMS_OUTPUT.PUT_LINE('Cursor has been closed.');
  END IF;
END;
```

What This Example Covers:
- Checks `%ISOPEN` before and after opening/closing the cursor
- Uses `%FOUND` and `%NOTFOUND` to control the loop
- Uses `%ROWCOUNT` to display the number of rows processed
- Safely closes the cursor at the end

## Cursor FOR Loop (Simplest)
This method lets Oracle handle OPEN, FETCH, and CLOSE automatically. Much cleaner, ideal for most use cases.

```
BEGIN
  FOR emp_rec IN (SELECT id, name FROM employees WHERE department_id = 10) LOOP
    DBMS_OUTPUT.PUT_LINE(emp_rec.id || ': ' || emp_rec.name);
  END LOOP;
END;
```

## Parameterized Cursors
You can pass parameters into cursors like functions.


```
DECLARE
  CURSOR emp_cur(p_dept_id NUMBER) IS
    SELECT id, name FROM employees WHERE department_id = p_dept_id;

  v_id employees.id%TYPE;
  v_name employees.name%TYPE;
BEGIN
  OPEN emp_cur(20);
  LOOP
    FETCH emp_cur INTO v_id, v_name;
    EXIT WHEN emp_cur%NOTFOUND;

    DBMS_OUTPUT.PUT_LINE(v_id || ': ' || v_name);
  END LOOP;
  CLOSE emp_cur;
END;
```

## Cursors + RECORD
You can use a RECORD instead of multiple variables.

```
DECLARE
  CURSOR emp_cur IS SELECT id, name FROM employees;
  v_emp_rec emp_cur%ROWTYPE;
BEGIN
  OPEN emp_cur;
  LOOP
    FETCH emp_cur INTO v_emp_rec;
    EXIT WHEN emp_cur%NOTFOUND;
    DBMS_OUTPUT.PUT_LINE(v_emp_rec.name);
  END LOOP;
  CLOSE emp_cur;
END;
```
