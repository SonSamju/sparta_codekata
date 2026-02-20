# 오랜 기간 보호한 동물(1)
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/59044
# 작성자: 손삼주
# 작성일: 2026. 02. 20. 17:52:01

select
    I.NAME,
    I.DATETIME
from ANIMAL_INS I LEFT JOIN ANIMAL_OUTS O
ON I.ANIMAL_ID = O.ANIMAL_ID
WHERE O.ANIMAL_ID IS NULL
ORDER BY I.DATETIME ASC
LIMIT 3
