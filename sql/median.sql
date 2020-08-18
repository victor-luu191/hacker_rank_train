select @median_row:=floor(count(*)/2)
from STATION;
-- 
select lat_n
from STATION
order by lat_n
limit @median_row;