select round(power(power(max(lat_n)- min(lat_n), 2) + power(max(long_w) - min(long_w), 2), 0.5), 4)
from STATION