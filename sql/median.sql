-- select @median_row:=floor(count(*)/2)
-- from STATION;
-- -- 
-- select lat_n
-- from STATION
-- order by lat_n
-- limit @median_row;

set @median_row = (select floor(count(*)/2) from STATION);
-- 
set @row = 0;
select (@row := @row + 1) as row_number 
    -- , lat_n
from STATION
-- order by lat_n;
