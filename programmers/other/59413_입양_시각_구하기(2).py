# 입양 시각 구하기(2)
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/59413
# 작성자: 손삼주
# 작성일: 2026. 03. 12. 15:11:33

WITH RECURSIVE cte AS (
    SELECT 0 as HOUR
    UNION ALL
    SELECT HOUR+1 AS HOUR 
    FROM cte
    WHERE HOUR < 23
)
SELECT
    c.HOUR,
    IFNULL(COUNT, 0) AS COUNT
FROM cte c 
LEFT JOIN (
    SELECT 
    HOUR(DATETIME) AS HOUR,
    COUNT(ANIMAL_ID) AS COUNT
    FROM ANIMAL_OUTS
    GROUP BY HOUR
    ) AS a
    ON c.HOUR = a.HOUR
ORDER BY HOUR
    



