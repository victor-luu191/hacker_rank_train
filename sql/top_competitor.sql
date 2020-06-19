select t5.hacker_id,
t5.name
from
(
select t4.hacker_id,
	Hackers.name,
	-- t4.n_full_score
from
	(
	select t3.hacker_id,
		t3.n_full_score
	from
		(
		select t2.hacker_id,
			sum(got_full_score) as n_full_score
		from
			(
			select t1.hacker_id,
				t1.challenge_id,
				hacker_score,
				t1.difficulty_level,
				if(hacker_score = Difficulty.score, 1, 0) as got_full_score
			from 
			-- join Submissions n Challenges to get difficulty_level
				(
				select Submissions.hacker_id, 
					Submissions.challenge_id,
					Submissions.score as hacker_score,
					Challenges.difficulty_level 
				from Submissions
				join Challenges
				on Submissions.challenge_id = Challenges.challenge_id
				) as t1
			-- join to check if hacker got full score
			join Difficulty
			on t1.difficulty_level = Difficulty.difficulty_level
			) as t2
		group by t2.hacker_id
		) as t3
	where t3.n_full_score > 1
	) as t4
join Hackers
on t4.hacker_id = Hackers.hacker_id
order by t4.n_full_score desc, t4.hacker_id
) as t5