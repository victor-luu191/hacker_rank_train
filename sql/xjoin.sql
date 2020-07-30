-- return  all such symmetric pairs in ascending order by the value of X

-- NOTE: pairs (x, x) can cause bug, because on x-join, a pair (x, x) will meet itself again, leading us to believe there is symmetric, while may be not. there is only symmetric if a pair (x,x) occur 2 times. so those pairs must be handled separately

select res.x, res.y
from
	(-- select symmetric pairs from pairs (x, y) with x < y
		(select t1.x1 as x, t1.y1 as y
		from
			(select f1.x as x1, f1.y as y1, f2.x as x2, f2.y as y2
			from
				(select * from functions where x < y) as f1
				cross join (select * from functions where x > y) as f2
			) as t1
		where t1.x1 = t1.y2 and t1.y1 = t1.x2
		) 
		union
		-- select symmetric pairs from pairs (x, x) which occur >= 2 times
		(select t3.x, t3.y
		from
			(select t2.x, t2.y, count(*) as count
			from
				(select * from functions where x=y) as t2
			group by t2.x, t2.y
			) as t3
		where t3.count > 1
		)
	) as res
order by res.x
