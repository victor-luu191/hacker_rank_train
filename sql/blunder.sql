-- short sol via tmp vars
set @actual_avg = (select avg(salary) from EMPLOYEES);
set @wrong_avg = (select avg(t0.wrong_sal) 
					from (select replace(cast(salary as char), '0', '') as wrong_sal
							from EMPLOYEES
							) as t0
					);
select ceiling(@actual_avg - @wrong_avg);
