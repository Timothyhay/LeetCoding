
-- INNER JOIN FOR MULTIPLE TIMES
-- https://www.hackerrank.com/challenges/placements/problem?isFullScreen=true
SELECT S.name
FROM Students S
JOIN Friends F ON S.ID = F.ID
JOIN Packages Ps ON S.ID = Ps.ID
JOIN Packages Pf ON F.Friend_ID = Pf.ID
AND Ps.Salary < Pf.Salary
ORDER BY Pf.Salary;