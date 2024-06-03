-- To handle null values in WHERE clauses, you should employ COALESCE on top of the column that has null values

SELECT
	COALESCE(department, "* NO DEPARTMENT *") as department,
	COUNT(salary) as total_employees
FROM employees
GROUP BY department
ORDER BY department

-- Department values should be grouped, having "* NO DEPARTMENT *" as the first result