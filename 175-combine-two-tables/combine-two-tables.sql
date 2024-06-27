# Write your MySQL query statement below
SELECT firstName, lastName, city, state
FROM person
left join address using(personid)