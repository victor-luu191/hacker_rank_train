-- template
SELECT first_column AS <first_column_alias>,
[pivot_value1], [pivot_value2], ... [pivot_value_n]
FROM 
(<source_table>) AS <source_table_alias>
PIVOT 
(
 aggregate_function(<aggregate_column>)
 FOR <pivot_column>
 IN ([pivot_value1], [pivot_value2], ... [pivot_value_n])
) AS <pivot_table_alias>;

-- output headers Doctor, Professor, Singer, and Actor
SELECT ["Doctor"], ["Professor"], ["Singer"], ["Actor"]
FROM 
(SELECT occupation, name FROM OCCUPATIONS) AS tmp
PIVOT 
(
 group_concat(name order by name)
 FOR occupation
 IN (["Doctor"], ["Professor"], ["Singer"], ["Actor"])
) AS pvt_table;

-- mysql has no pivot operator
SELECT *
FROM (
    SELECT group_concat(if(occupation = "Doctor", name, null) ),
            group_concat(if(occupation = "Professor", name, null) ),
            group_concat(if(occupation = "Singer", name, null) ),
            group_concat(if(occupation = "Actor", name, null) )
    FROM OCCUPATIONS 
) AS pvt_table;