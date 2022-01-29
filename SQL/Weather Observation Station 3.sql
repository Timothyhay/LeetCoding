--== SELECT --==

-- Query a list of CITY names from STATION for cities that have an even ID number. Print the results in any order, but exclude duplicates from the answer.

SELECT DISTINCT CITY FROM STATION
WHERE ID % 2 = 0;


-- Find the difference between the total number of CITY entries in the table and the number of distinct CITY entries in the table.

SELECT (COUNT(CITY) - COUNT(DISTINCT CITY)) FROM STATION;


-- Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths (i.e.: number of characters in the name). If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.

(SELECT CITY, LENGTH(CITY) FROM STATION 
ORDER BY LENGTH(CITY) ASC, CITY LIMIT 1)
UNION
(SELECT CITY, LENGTH(CITY) FROM STATION 
ORDER BY LENGTH(CITY) DESC, CITY LIMIT 1);


-- Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION. Your result cannot contain duplicates.

SELECT DISTINCT CITY FROM STATION
WHERE CITY RLIKE '^[aeiou]';
-- ^	匹配输入字符串的开始位置，除非在方括号表达式中使用，当该符号在方括号表达式中使用时，表示不接受该方括号表达式中的字符集合。要匹配 ^ 字符本身，请使用 \^。
-- LIKE for only _ and $

-- Query the list of CITY names ending with vowels (a, e, i, o, u) from STATION. Your result cannot contain duplicates.

SELECT DISTINCT CITY FROM STATION
WHERE CITY RLIKE '[aeiou]$'



-- Query the Name of any student in STUDENTS who scored higher than  Marks. Order your output by the last three characters of each name. If two or more students both have names ending in the same last three characters (i.e.: Bobby, Robby, etc.), secondary sort them by ascending ID.

SELECT Name FROM STUDENTS
WHERE Marks>75 ORDER BY RIGHT(Name, 3) ASC, ID ASC;


/*
Samantha was tasked with calculating the average monthly salaries for all employees in the EMPLOYEES table, but did not realize her keyboard's  key was broken until after completing the calculation. She wants your help finding the difference between her miscalculation (using salaries with any zeros removed), and the actual average salary.

Write a query calculating the amount of error (i.e.:  average monthly salaries), and round it up to the next integer.
*/
SELECT CEIL(AVG(Salary) - AVG(REPLACE(Salary, 0, ''))) FROM EMPLOYEES 


/*
We define an employee's total earnings to be their monthly  worked, and the maximum total earnings to be the maximum total earnings for any employee in the Employee table. Write a query to find the maximum total earnings for all employees as well as the total number of employees who have maximum total earnings. Then print these values as  space-separated integers.

*/
SELECT months*salary AS Earning, COUNT(*) FROM Employee 
GROUP BY Earning
ORDER BY Earning DESC
LIMIT 1;


/*
Write a query identifying the type of each record in the TRIANGLES table using its three side lengths. Output one of the following statements for each record in the table:

Equilateral: It's a triangle with  sides of equal length.
Isosceles: It's a triangle with  sides of equal length.
Scalene: It's a triangle with  sides of differing lengths.
Not A Triangle: The given values of A, B, and C don't form a triangle.
*/

SELECT CASE 
        WHEN A + B > C AND B + C > A AND A + C > B THEN
            CASE 
                WHEN A = B AND B = C THEN 'Equilateral' 
                WHEN A = B OR A = C OR B = C THEN 'Isosceles'
                ELSE 'Scalene'
            END
        ELSE 'Not A Triangle'
    END
    FROM TRIANGLES;




-- CONCAT String
/*
Generate the following two result sets:

Query an alphabetically ordered list of all names in OCCUPATIONS, immediately followed by the first letter of each profession as a parenthetical (i.e.: enclosed in parentheses). For example: AnActorName(A), ADoctorName(D), AProfessorName(P), and ASingerName(S).
Query the number of ocurrences of each occupation in OCCUPATIONS. Sort the occurrences in ascending order, and output them in the following format:

There are a total of [occupation_count] [occupation]s.
*/

SELECT CONCAT(Name, '(', LEFT(Occupation, 1), ')') FROM OCCUPATIONS
ORDER BY Name;

SELECT CONCAT('There are a total of ', COUNT(Occupation),' ', lower(Occupation), 's.') FROM OCCUPATIONS
GROUP BY Occupation ORDER BY COUNT(Occupation) ASC;



/*
Pivot the Occupation column in OCCUPATIONS so that each Name is sorted alphabetically and displayed underneath its corresponding Occupation. The output column headers should be Doctor, Professor, Singer, and Actor, respectively.

Note: Print NULL when there are no more names corresponding to an occupation.
*/

set @r1=0, @r2=0, @r3=0, @r4=0;
select min(Doctor), min(Professor), min(Singer), min(Actor)
from(
  select case when Occupation='Doctor' then (@r1:=@r1+1)
            when Occupation='Professor' then (@r2:=@r2+1)
            when Occupation='Singer' then (@r3:=@r3+1)
            when Occupation='Actor' then (@r4:=@r4+1) end as RowNumber,
    case when Occupation='Doctor' then Name end as Doctor,
    case when Occupation='Professor' then Name end as Professor,
    case when Occupation='Singer' then Name end as Singer,
    case when Occupation='Actor' then Name end as Actor
  from OCCUPATIONS
  order by Name
	) temp
group by RowNumber;



/*
You are given a table, BST, containing two columns: N and P, where N represents the value of a node in Binary Tree, and P is the parent of N.

Write a query to find the node type of Binary Tree ordered by the value of the node. Output one of the following for each node:

Root: If node is root node.
Leaf: If node is leaf node.
Inner: If node is neither root nor leaf node.

*/
SELECT CASE 
    WHEN P IS NULL THEN CONCAT(N, ' Root')
    WHEN N IN (SELECT DISTINCT P FROM BST) THEN CONCAT(N, ' Inner')
    ELSE CONCAT(N, ' Leaf')
    END
FROM BST ORDER BY N ASC;

/*
Given the table schemas below, write a query to print the company_code, founder name, total number of lead managers, total number of senior managers, total number of managers, and total number of employees. Order your output by ascending company_code.

Note:

The tables may contain duplicate records.
The company_code is string, so the sorting should not be numeric. For example, if the company_codes are C_1, C_2, and C_10, then the ascending company_codes will be C_1, C_10, and C_2.
*/
SELECT c.company_code, c.founder, COUNT(DISTINCT l.lead_manager_code), COUNT(DISTINCT s.senior_manager_code), COUNT(DISTINCT m.manager_code), COUNT(DISTINCT E.employee_code )
FROM Company c, Lead_Manager l, Senior_Manager s, Manager m, Employee e
WHERE c.company_code=l.company_code 
AND l.lead_manager_code=s.lead_manager_code 
AND s.senior_manager_code=m.senior_manager_code 
AND m.manager_code=e.manager_code
GROUP BY c.company_code, c.founder 
ORDER BY c.company_code ASC


--== Aggregation ==--
-- Query the Western Longitude (LONG_W) for the largest Northern Latitude (LAT_N) in STATION that is less than . Round your answer to  decimal places.

SELECT ROUND(LONG_W, 4)
FROM STATION
WHERE LAT_N = (SELECT MAX(LAT_N) FROM STATION WHERE LAT_N < 137.2345)



-- A median is defined as a number separating the higher half of a data set from the lower half. Query the median of the Northern Latitudes (LAT_N) from STATION and round your answer to  decimal places.

SELECT ROUND(S.LAT_N, 4) FROM STATION S
WHERE (SELECT COUNT(LAT_N) FROM STATION WHERE LAT_N < S.LAT_N) = (SELECT COUNT(LAT_N) FROM STATION WHERE LAT_N > S.LAT_N)



-- Ketty gives Eve a task to generate a report containing three columns: Name, Grade and Mark. Ketty doesn't want the NAMES of those students who received a grade lower than 8. The report must be in descending order by grade -- i.e. higher grades are entered first. If there is more than one student with the same grade (8-10) assigned to them, order those particular students by their name alphabetically. Finally, if the grade is lower than 8, use "NULL" as their name and list them by their grades in descending order. If there is more than one student with the same grade (1-7) assigned to them, order those particular students by their marks in ascending order.
-- INNER JOIN == JOIN == WHERE a.id = b.pid

SELECT IF(Grade>=8, Name, NULL), Grade, Marks
FROM Students INNER JOIN Grades 
WHERE MARKS BETWEEN Min_Mark AND Max_Mark
ORDER BY Grade DESC, Name ASC


-- 在 SQL 中增加 HAVING 子句原因是，WHERE 关键字无法与聚合函数一起使用。
-- HAVING 子句可以让我们筛选分组后的各组数据。



-- 在同样 power, age (W.power = WT.power AND P.age = PT.age) 情况下选择 coins_needed 最少的

SELECT id, age, coins_needed, power
FROM Wands W, Wands_Property P
WHERE W.code = P.code AND P.is_evil = 0 AND W.coins_needed = (
SELECT MIN(coins_needed)
FROM Wands WT, Wands_Property PT
WHERE WT.code = PT.code AND W.power = WT.power AND P.age = PT.age
)
ORDER BY power DESC, age DESC



SELECT h.hacker_id, name, sum(maxs) totalscore
FROM Hackers AS h INNER JOIN
    (SELECT hacker_id, MAX(score) maxs FROM Submissions
      GROUP BY hacker_id, challenge_id) AS temp
  ON h.hacker_id = temp.hacker_id
GROUP BY h.hacker_id, h.name
HAVING totalscore > 0
ORDER BY totalscore DESC, temp.hacker_id
