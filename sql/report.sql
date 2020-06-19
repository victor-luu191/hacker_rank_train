SELECT 
	CASE
		when grade < 8 then null
		else Students.name
	END as name, 
	mg.grade as grade, 
	Students.marks as mark
FROM Students
JOIN
(SELECT marks,
CASE
	when (marks >= 0) and (marks < 10) then 1
	when (marks >= 10) and (marks < 20) then 2
	when (marks >= 20) and (marks < 30) then 3
	when (marks >= 30) and (marks < 40) then 4
	when (marks >= 40) and (marks < 50) then 5
	when (marks >= 50) and (marks < 60) then 6
	when (marks >= 60) and (marks < 70) then 7
	when (marks >= 70) and (marks < 80) then 8
	when (marks >= 80) and (marks < 90) then 9
	else 10
END as grade
FROM Students) as mg
ON Students.marks = mg.marks
order by grade desc, name, mark