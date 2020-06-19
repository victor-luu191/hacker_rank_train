-- if WITH is supported
WITH cte as 
(SELECT a.N as N, a.P as P, b.C as C
FROM BST as a
left join  (SELECT P as N, N as C FROM BST) as b
on a.N = b.N
)
SELECT cte.N,
case 
    when cte.P is null then "Root"
    when cte.C is null then "Leaf"
    when (cte.P is not null) and (cte.C is not null) then "Inner"
end node_type
FROM cte
order by cte.N

-- WITH is not supported
SELECT cte.N,
CASE
    when cte.P is null then "Root"
    when cte.C is null then "Leaf"
    when (cte.P is not null) and (cte.C is not null) then "Inner"
END node_type
FROM
(SELECT a.N as N, a.P as P, b.C as C
FROM BST as a
left join  (SELECT P as N, N as C FROM BST) as b
on a.N = b.N
) as cte