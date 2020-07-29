--  total score of a hacker is the sum of his maximum scores 
-- for all of the challenges. 
-- for each challenge, a hacker can have several submissions and we only
-- care abt the max score for the challenge

select res.hacker_id, res.name, res.total_score
from
	(select hackers.hacker_id, hackers.name, t2.total_score
	from
		(select t1.hacker_id, sum(t1.max_score) as total_score
		from
			(select hacker_id, challenge_id, max(score) as max_score
			from Submissions
			group by hacker_id, challenge_id
			) as t1
		group by t1.hacker_id
		) as t2
	join hackers
	on t2.hacker_id = hackers.hacker_id
	) as res
where res.total_score > 0
order by res.total_score desc, res.hacker_id


