# 📘 Comprehensive Excel Formulas Cheat Sheet

This document contains a structured reference of the **most commonly used and advanced Excel formulas**, organized by category, with **syntax, explanations, and examples**.

---

## 1. Math & Trig
- **`=SUM(A1:A10)`** → Adds all numbers in range.  
  *Example:* If A1:A5 = {2,3,5,7,10} → **27**
- **`=ROUND(A1,2)`** → Rounds value to 2 decimals.  
  *Example:* 12.345 → **12.35**
- **`=ROUNDUP(A1,0)`** → Always rounds up.  
- **`=ROUNDDOWN(A1,0)`** → Always rounds down.
- **`=ABS(A1)`** → Returns absolute value.  
- **`=MOD(A1,3)`** → Returns remainder after division.
- **`=POWER(A1,2)`** → A1 squared.
- **`=SUMPRODUCT(A1:A5,B1:B5)`** → Multiplies corresponding items and sums.  
  *Example:* A={2,3}, B={4,5} → 2×4 + 3×5 = **23**

---

## 2. Statistical
- **`=AVERAGE(A1:A10)`** → Mean value.
- **`=MEDIAN(A1:A10)`** → Middle value.
- **`=MODE(A1:A10)`** → Most frequent value.
- **`=STDEV.S(A1:A10)`** → Sample standard deviation.
- **`=VAR.S(A1:A10)`** → Sample variance.
- **`=RANK(A1,A1:A10,0)`** → Rank of a number.
- **`=CORREL(A1:A10,B1:B10)`** → Correlation between 2 datasets.
- **`=COUNTIF(A1:A10,">10")`** → Count cells matching one condition.
- **`=COUNTIFS(A1:A10,">10",B1:B10,"<5")`** → Count cells matching multiple conditions.
- **`=SUMIF(A1:A10,">10",B1:B10)`** → Sum values in B where A > 10.
- **`=SUMIFS(C1:C10,A1:A10,">10",B1:B10,"<5")`** → Sum values in C with multiple conditions.

---

## 3. Text Functions
- **`=CONCAT(A1,B1)`** → Joins values.  *Example:* “Excel” + “Pro” → “ExcelPro”.
- **`=TEXT(A1,"MM/DD/YYYY")`** → Format as date.
- **`=LEFT(A1,4)`** → First 4 chars.  
- **`=RIGHT(A1,3)`** → Last 3 chars.
- **`=LEN(A1)`** → Character count.
- **`=SEARCH("Pro",A1)`** → Finds position of substring.
- **`=SUBSTITUTE(A1,"old","new")`** → Replace text.
- **`=PROPER(A1)`** → Capitalize words.

---

## 4. Logical
- **`=IF(A1>50,"Pass","Fail")`** → Conditional test.
- **`=AND(A1>0,B1<100)`** → Both must be TRUE.
- **`=OR(A1>0,B1<100)`** → At least one TRUE.
- **`=NOT(A1>50)`** → Reverses logic.
- **`=IFS(A1>90,"A", A1>80,"B", TRUE,"C")`** → Multiple IFs simplified.

---

## 5. Lookup & Reference
- **`=VLOOKUP(40,A2:C10,2,FALSE)`** → Searches first column.
- **`=HLOOKUP(40,A1:J2,2,FALSE)`** → Searches first row.
- **`=INDEX(A1:C10,2,3)`** → Returns value at row 2, col 3.
- **`=MATCH(50,A1:A10,0)`** → Position of 50 in list.
- **`=XLOOKUP(40,A2:A10,B2:B10,"Not found")`** → Modern replacement for VLOOKUP.
- **`=INDEX(B1:B10,MATCH("Apple",A1:A10,0))`** → INDEX + MATCH combo for flexible lookups.
- **`=OFFSET(A1,2,3)`** → Reference cell 2 down, 3 right.
- **`=CHOOSE(2,"Red","Blue","Green")`** → Returns 2nd item → “Blue”.
- **`=INDIRECT("A"&B1)`** → Returns reference from text. If B1=5 → Returns A5.

---

## 6. Advanced Lookup & Analysis
- **Multi-Criteria Lookup (INDEX + MATCH + multiple conditions):**  
  `=INDEX(C2:C10,MATCH(1,(A2:A10=E1)*(B2:B10=E2),0))`  
  Returns value from column C where A=E1 and B=E2.

- **Dynamic Dependent Dropdowns with INDIRECT:**  
  Use `=INDIRECT(A1)` in Data Validation so that choice in A1 determines dropdown list.

- **3D Formula Across Sheets:**  
  `=SUM(Sheet1:Sheet3!A1)` → Sums A1 across Sheet1 to Sheet3.

- **Dynamic Ranges with OFFSET:**  
  `=SUM(OFFSET(A1,0,0,B1,1))` → Sums a dynamic range based on value in B1.

- **Nested Lookups:**  
  `=XLOOKUP(D1,A1:A10,XLOOKUP(D2,B1:B10,C1:C10))` → Double lookup.

- **Dynamic Named Ranges:**  
  Using `=OFFSET($A$1,0,0,COUNTA($A:$A),1)` to auto-expand as data grows.

---

## 7. Date & Time
- **`=TODAY()`** → Current date.
- **`=NOW()`** → Current date & time.
- **`=DAY(A1)`** → Extract day.
- **`=MONTH(A1)`** → Extract month.
- **`=YEAR(A1)`** → Extract year.
- **`=EOMONTH(A1,1)`** → End of next month.
- **`=NETWORKDAYS(A1,A2)`** → Business days between.
- **`=DATEDIF(A1,A2,"Y")`** → Years difference.
- **`=WORKDAY(A1,5)`** → Date after 5 workdays.

---

## 8. Financial
- **`=PMT(5%/12,60,30000)`** → Monthly loan payment.
- **`=FV(6%,10,-500)`** → Future value of yearly $500 deposits.
- **`=NPV(10%,A2:A10)`** → Net present value.
- **`=XNPV(10%,values,dates)`** → NPV with irregular dates.
- **`=XIRR(values,dates)`** → IRR for irregular cashflows.
- **`=IPMT(rate,period,nper,pv)`** → Interest portion of payment.

---

## 9. Dynamic Array Functions
- **`=UNIQUE(A1:A20)`** → Extract unique values.
- **`=SORT(A1:A20,1,TRUE)`** → Sort ascending.
- **`=FILTER(A1:B20,B1:B20>100)`** → Filter by condition.
- **`=SEQUENCE(10,1,1,1)`** → Generate sequence 1–10.
- **`=RANDARRAY(5,1,1,100,TRUE)`** → Random numbers 1–100.
- **`=TEXTSPLIT(A1,",")`** → Split text into columns.

---

## 10. Information Functions
- **`=ISNUMBER(A1)`** → TRUE if number.
- **`=ISTEXT(A1)`** → TRUE if text.
- **`=ISERROR(A1)`** → TRUE if error.
- **`=IFERROR(A1,"N/A")`** → Replace error with text.
- **`=TYPE(A1)`** → Returns type of value.

---

## 11. Database Functions
- **`=DSUM(Database,"Sales",Criteria)`** → Sum values meeting criteria.
- **`=DAVERAGE(Database,"Cost",Criteria)`** → Average meeting criteria.
- **`=DCOUNT(Database,"ID",Criteria)`** → Count entries.

---

## Best Practices
- Use **named ranges** for readability.
- Prefer **XLOOKUP/INDEX-MATCH** over VLOOKUP.
- Use **dynamic arrays** instead of legacy arrays.
- Combine formulas with **conditional formatting** for dashboards.
- Apply **structured references** in tables for clarity.
- Use **INDIRECT & OFFSET carefully**—they are volatile and can slow down large workbooks.

---

