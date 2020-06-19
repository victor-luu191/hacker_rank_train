select abc.company_code, abc.founder, abc.n_lead_man, abc.n_senior_man, 
	e.n_manager, e.n_employee
from 
(select ab.company_code, ab.founder, ab.n_lead_man, c.n_senior_man
from
(select a.company_code, a.founder, b.n_lead_man 
from Company as a
join (select company_code, count(*) as n_lead_man
from Lead_Manager 
group by company_code
) as b
on a.company_code = b.company_code) as ab
join (select company_code, count(*) as n_senior_man
	from Senior_Manager
	group by company_code 
) as c
on ab.company_code = c.company_code) as abc
join (select company_code, 
		count(distinct manager_code) as n_manager, 
		count(distinct employee_code) as n_employee
		from Employee
		group by company_code
) as e
on abc.company_code = e.company_code
order by e.company_code