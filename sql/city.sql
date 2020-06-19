-- find city with shortest name
select city, city_len
from
(select city, len(city) as city_len
from STATION) as a
order by a.city_len, a.city
limit 1;

-- city with longest name
select city, city_len
from
(select city, len(city) as city_len
from STATION) as a
order by a.city_len desc, a.city
limit 1;