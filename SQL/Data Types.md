# SQL Data Types
#### [Back to Main]

## General SQL Data Types Categories:

### Numeric Types:
- **INTEGER**: A whole number without a fractional component.
- **SMALLINT**: A smaller whole number, typically with a smaller range than INTEGER.
- **BIGINT**: A larger whole number, with a larger range than INTEGER.
- **DECIMAL/NUMERIC**: Fixed-point numbers with user-specified precision and scale (total digits and decimal places).
- **FLOAT**: Floating-point numbers with binary precision.
- **REAL**: A single-precision floating-point number.
- **DOUBLE PRECISION**: A double-precision floating-point number.

### Character String Types:
- **CHAR**: Fixed-length character string.
- **VARCHAR**: Variable-length character string with a specified maximum length.
- **TEXT**: Variable-length character string with no specified maximum length.

### Date and Time Types:
- **DATE**: Date without a time component.
- **TIME**: Time without a date component.
- **TIMESTAMP**: Date and time, often including fractional seconds.
- **INTERVAL**: A duration of time.

### Boolean Type:
- **BOOLEAN/BOOL**: Represents true or false values.
- **Binary Types**:
- **BINARY**: Fixed-length binary data.
- **VARBINARY**: Variable-length binary data.
- **BLOB (Binary Large Object)**: Stores large binary data, like images or documents.

### Other Types:
- **CLOB (Character Large Object)**: Stores large character data.
- **XML**: Stores XML data.
- **JSON**: Stores JSON-formatted data.

Custom Types:
- User-defined or custom data types created by the database designer.

## Platform-Specific Data Types:

### MySQL:
- **TINYINT**: Small integer, often used for flags (range: -128 to 127).
- **MEDIUMINT**: Medium-sized integer.
- **DATETIME**: Date and time with a fractional seconds part.
- **ENUM**: Enumerated types.
- **SET**: A set of values chosen from a predefined list.

### MS SQL:
- **TINYINT**: Small integer.
- **SMALLDATETIME**: Date and time with a smaller range.
- **DATETIME2**: Date and time with a fractional seconds part and an extended range.
- **UNIQUEIDENTIFIER**: Globally unique identifier (GUID).
- **XML**: Stores XML data.
- **HIERARCHYID**: Represents position in a hierarchy.

### Oracle Database:
- **NUMBER**: Variable precision number.
- **RAW**: Variable-length binary data.
- **TIMESTAMP WITH TIME ZONE**: Date and time with time zone information.
- **TIMESTAMP WITH LOCAL TIME ZONE**: Date and time with local time zone information.
- **BLOB**: Binary Large Object.
- **CLOB**: Character Large Object.

### PostgreSQL:
- **SERIAL/BIGSERIAL**: Auto-incrementing integer.
- [**UUID**]: Universally Unique Identifier.
- **MONEY**: Currency amount.
- **INTERVAL**: A duration of time.
- **JSONB**: Binary JSON.

### SQLite:
- **INTEGER (AUTOINCREMENT)**: Auto-incrementing integer.
- **REAL**: Floating-point number.
- **TEXT**: Textual data.
- **BLOB**: Binary Large Object.

### IBM Db2:
- **SMALLINT/INTEGER/BIGINT**: Various integer types.
- **DECFLOAT**: Decimal floating-point number.
- **XML**: Stores XML data.
- **ROWID**: Represents the unique identifier for a row in a table.

### MariaDB:
- **TINYINT/MEDIUMINT/YEAR**: Various integer types.
- **JSON**: Stores JSON-formatted data.
- **TINYBLOB**: Tiny Binary Large Object.
- **GEOMETRY**: Spatial data type.

### BigQuery:
- **INT64/FLOAT64**: Integer and floating-point numbers.
- **TIMESTAMP**: Date and time.
- **DATE**: Date without a time component.
- **BOOL**: Boolean values.
- **BYTES**: Binary data.
