-- short sol via user-defined vars
-- ========================================
set @max_earn = (select max(salary * months) from Employee);

-- count number of employees having total earn equals to a specific value
select total_earn, count(*)
from
    (select employee_id, 
        salary * months as total_earn
    from Employee
    ) as t0
group by total_earn
having total_earn=@max_earn;
