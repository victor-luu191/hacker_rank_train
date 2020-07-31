-- if End_Date of the tasks are consecutive, then they are part of the same project
-- output the start and end dates of projects listed by the number of days it took to complete the project in ascending order

-- between transfer from one project to a new one, there will be a break > 1 day --> diff > 1

select t4.project_start, t4.project_end
from
	(select *
		, t3.project_end - t3.project_start as n_day
	from
		(select t2.project_start
			, lead(t2.prev_project_end) over (order by -t2.project_start desc) as project_end
		from
			(select  t1.end_date_prev_task as prev_project_end
				, t1.start_date as project_start		
			from
				(select  start_date
					, end_date
					, lag(end_date) over (order by -start_date desc) as end_date_prev_task
					, end_date - (lag(end_date) over (order by -start_date desc)) as diff
				from 
					-- add a dummy row at the end to ensure that the last project has (dummy) next project, so that the last project also has mark
					((select * from projects) union (select null, null, null)) as t0
				) as t1
			where (t1.diff is null) or (t1.diff > 1)	-- marker of a new project
			) as t2
		) as t3
	) as t4
where t4.project_start is not null
order by t4.n_day, t4.project_start


-- can also try  finding start date via local var

