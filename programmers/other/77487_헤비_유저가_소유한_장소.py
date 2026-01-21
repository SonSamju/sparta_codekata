# 헤비 유저가 소유한 장소
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/77487
# 작성자: 손삼주
# 작성일: 2026. 01. 21. 10:18:32

-- 코드를 입력하세요
WITH HEAVY_USER AS 
(SELECT
    HOST_ID,
    COUNT(*) AS CNT_SPACE
FROM PLACES S
GROUP BY HOST_ID
HAVING CNT_SPACE >=2
)
SELECT
    ID,
    NAME,
    HOST_ID
FROM PLACES P
WHERE EXISTS (
SELECT 1
FROM HEAVY_USER H
WHERE P.HOST_ID = H.HOST_ID)