-- output the names of those students whose best friends got offered a higher salary than them. Names must be ordered by the salary amount offered to the best friends.

select t3.name
from
	(select *
	from
		(select t1.id as student_id, t1.friend_id, t1.student_salary, packages.salary as friend_salary
		from
			(select friends.id, friends.friend_id, packages.salary as student_salary
			from friends 
			join packages
			on friends.id = packages.id
			) as t1
		join packages
		on t1.friend_id = packages.id
		) as t2
	join students
	on students.id = t2.student_id
	) as t3
where t3.friend_salary > t3.student_salary
order by t3.friend_salary


