select 
	case 
		when t.a = t.b and t.b = t.c then "Equilateral"
		when (t.a = t.b and t.b != t.c and t.c < t.a + t.b) then "Isosceles"
		when (t.a = t.c and t.c != t.b and t.b < t.a + t.c) then "Isosceles"
		when (t.b = t.c and t.c != t.a and t.a < t.b + t.c) then "Isosceles"
		when (t.a != t.b and t.b != t.c and t.c != t.a and t.a < t.b + t.c and t.b < t.a + t.c and t.c < t.a + t.b) then "Scalene"
		else "Not A Triangle"
	end
from triangles as t