# Power BI DAX Functions Cheat Sheet

## 1. Aggregation & Statistical Functions
- **SUM(column)** — Sum of all values in a column  
- **SUMX(table, expression)** — Sum of evaluated expression across rows  
- **AVERAGE(column)** / **AVERAGEX(table, expression)** — Average value  
- **COUNT**, **COUNTA**, **COUNTROWS** — Count rows or non-blank entries  
- **MIN**, **MAX** — Minimum and maximum values  

---

## 2. Mathematical & Trigonometric Functions
Includes **ABS**, **ACOS**, **ASIN**, **ROUND**, **STDEV**, **VAR**, and more.  

---

## 3. Date & Time / Time Intelligence
- **DATE**, **YEAR**, **MONTH**, **DAY**, **NOW**, **TODAY**  
- Time Intelligence: **DATESYTD**, **TOTALYTD**, **SAMEPERIODLASTYEAR**, **DATEADD**, **DATEDIFF**  

---

## 4. Logical, Information & Operators
- **IF**, **SWITCH**, **NOT** — Conditional logic  
- **ISTEXT**, **ISNUMBER**, **ISBLANK** — Data type checks  
- Operators: `+`, `-`, `*`, `/`, `&&`, `||`, etc.  

---

## 5. Text Functions
- **CONCATENATE**, **UPPER**, **LOWER**, **PROPER**, **LEN**, **SUBSTITUTE**, **REPLACE**  

---

## 6. Lookup & Relationship Functions
- **LOOKUPVALUE** — Fetch values from another table  
- **RELATED** — Get values via table relationships  

---

## 7. Filter & Context Functions
- **FILTER(table, condition)** — Filter rows based on condition  
- **CALCULATE(expression, filters...)** — Modify filter context for calculations  
- **ALL**, **ALLEXCEPT**, **ALLSELECTED** — Control context removal or preservation  

---

## 8. Ranking & Iterators
- **RANKX(table, expression)** — Rank values in a table  
- **X functions (e.g., SUMX, AVERAGEX, COUNTX, MINX, MAXX)** — Row-wise evaluation across tables  

---

## 9. Advanced & Others
- **CALCULATETABLE** — Returns filtered table  
- **RELATEDTABLE**, **SUMMARIZE**, **ADDCOLUMNS** — Table manipulation and enrichment  

---

## Top 10 Most Used DAX Functions
1. **CALCULATE**  
2. **SUM**, **SUMX**  
3. **CALCULATETABLE**  
4. **RANKX**  
5. **DATEDIFF**  
6. **DATEADD**  
7. **COUNT**, **COUNTROWS**  
8. **LOOKUPVALUE**  
9. **FILTER**  
10. **RELATED**  

---

## Quick Reference Table

| Category                       | Key Functions |
|--------------------------------|---------------|
| Aggregation & Stats            | SUM*, AVERAGE*, COUNT*, MIN, MAX |
| Math & Stats                   | ROUND, ABS, STDEV, VAR, ACOS… |
| Date/Time + Time Intelligence  | DATE, NOW, TODAY, DATESYTD, SAMEPERIODLASTYEAR, DATEADD |
| Logical / Info / Operators     | IF, SWITCH, ISTEXT, ISBLANK, +, -, &&, || |
| Text                           | CONCATENATE, UPPER, LEN, REPLACE |
| Lookup / Relationship          | LOOKUPVALUE, RELATED |
| Filter & Context               | FILTER, CALCULATE, ALL, ALLEXCEPT |
| Ranking & Iterators            | RANKX, SUMX, AVERAGEX, COUNTX, MINX, MAXX |
| Advanced & Table Manipulation  | CALCULATETABLE, ADDCOLUMNS, RELATEDTABLE, SUMMARIZE |

---

### Resources
- Microsoft official DAX reference: https://learn.microsoft.com/en-us/dax/dax-function-reference  
- Community resource: https://dax.guide  
- Pragmatic Works Cheat Sheet: https://pragmaticworks.com/resources/cheat-sheet/dax  
