-- this challenge shows a trick of using a dummy to find and populate max value (of a field) to all rows of a table

select *
from
	(select Hackers.hacker_id, Hackers.name, t8.n_challenge
	from Hackers
	join
		(select t7.*
		from
			(select t5.*, t6.n_student
				from
					-- find max_n_challenge and populate it to all hacker, via a dummy
					(select t4.hacker_id, t4.n_challenge, 
						t3.max_n_challenge
					from
						(select cte1.*, 1 as dummy
						from
							(select hacker_id, count(challenge_id ) as n_challenge
							from challenges
							group by hacker_id) as cte1
						) as t4
					join
					(select max(t2.n_challenge) as max_n_challenge, 
						max(t2.dummy) as dummy
					from
						(select cte1.n_challenge, 1 as dummy
						from
							(select hacker_id, count(challenge_id ) as n_challenge
							from challenges
							group by hacker_id) as cte1) as t2
					) as t3
					on t4.dummy = t3.dummy
					) as t5
				join
					-- join to find out how many students create a given  n_challenge
					(select cte1.n_challenge, count(cte1.hacker_id) as n_student
					from
						(select hacker_id, count(challenge_id ) as n_challenge
						from challenges
						group by hacker_id) as cte1
					group by cte1.n_challenge
					) as t6
				on t5.n_challenge = t6.n_challenge
			) as t7
		where t7.n_student = 1 or (t7.n_student > 1 and t7.n_challenge = t7.max_n_challenge)
		) as t8
	on Hackers.hacker_id = t8.hacker_id) as t9
order by t9.n_challenge desc, t9.hacker_id
