-- output: contest_id, hacker_id, name, and the sums of total_submissions, total_accepted_submissions, total_views, and total_unique_views

select Contests.*, 
	t5.sum_total_submissions, 
	t5.sum_total_accepted_submissions,
	t5.sum_total_views,
	t5.sum_total_unique_views
from Contests
join
	(select t4.contest_id,
		sum(t4.total_submissions) as sum_total_submissions,
		sum(t4.total_accepted_submissions) as sum_total_accepted_submissions,
		sum(t4.total_views) as sum_total_views,
		sum(t4.total_unique_views) as sum_total_unique_views
	from
		(select t3.*, 
			Submission_Stats.total_submissions, 
			Submission_Stats.total_accepted_submissions
		from
			(select t12.*, View_Stats.total_views, View_Stats.total_unique_views
			from
				-- join tables Challenges and Colleges to see a challenge is selected in which contest(s)
				(select distinct t1.contest_id, t2.challenge_id
				from Colleges as t1 
				join Challenges as t2
				on t1.college_id = t2.college_id
				) as t12
			join View_Stats
			on t12.challenge_id = View_Stats.challenge_id
			) as t3
		join Submission_Stats
		on t3.challenge_id = Submission_Stats.challenge_id
		) as t4
	group by t4.contest_id
	having sum_total_views + sum_total_unique_views + sum_total_submissions + sum_total_accepted_submissions > 0
	) as t5
on Contests.contest_id = t5.contest_id