-- this challenge is an example of how we find the entry achieving min/max in each group (like argmin/argmax)

select w1.*
from
	-- add age column to wands
	(select Wands.id, Wands_Property.age, Wands.coins_needed, Wands.power
	from Wands join
		Wands_Property
	on Wands.code = Wands_Property.code
	where Wands_Property.is_evil = 0
	) as w1
join
-- find min gold for each combi (power, age)
(select t1.age, t1.power, min(t1.coins_needed) as min_gold
from 
	(select Wands_Property.age,  Wands.power, Wands.coins_needed
	from Wands join
		Wands_Property
	on Wands.code = Wands_Property.code
	where Wands_Property.is_evil = 0
	order by Wands.power desc, Wands_Property.age desc
	) as t1
group by t1.power, t1.age) as t2
on w1.power = t2.power and w1.age = t2.age and w1.coins_needed = t2.min_gold
order by w1.power desc, w1.age desc


