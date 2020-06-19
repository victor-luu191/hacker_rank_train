select concat(name, "(", substr(occupation, 1, 1), ")")
from OCCUPATIONS 
order by name;

select concat("There are a total of ", counts, occupation, "s")
from (select count(*) as counts, occupation
from OCCUPATIONS
group by occupation
) b
order by counts
