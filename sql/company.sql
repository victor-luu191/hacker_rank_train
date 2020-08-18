select *
from
	(select abcd.company_code, abcd.founder, 
		abcd.n_lead_man, abcd.n_senior_man, abcd.n_manager,
		e.n_employee
	from
		(select abc.company_code, abc.founder, abc.n_lead_man, abc.n_senior_man, 
			d.n_manager
		from 
			(select ab.company_code, ab.founder, ab.n_lead_man, c.n_senior_man
			from
				(select a.company_code, a.founder, b.n_lead_man 
				from Company as a
				join 
					(select company_code, count(distinct lead_manager_code ) as n_lead_man
					from Lead_Manager 
					group by company_code
					) as b
				on a.company_code = b.company_code
				) as ab
			join 
				(select company_code, count(distinct senior_manager_code ) as n_senior_man
					from Senior_Manager
					group by company_code 
				) as c
			on ab.company_code = c.company_code
			) as abc
		join 
			(select company_code, 
				count(distinct manager_code) as n_manager 
			from Manager
			group by company_code
			) as d
		on abc.company_code = d.company_code
		) as abcd
	join
		(select company_code, count(distinct employee_code ) as n_employee
			from Employee
			group by company_code
		) as e
	on abcd.company_code = e.company_code
	) as res
order by res.company_code