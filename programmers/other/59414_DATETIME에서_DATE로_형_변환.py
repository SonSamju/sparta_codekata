# DATETIME에서 DATE로 형 변환
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/59414
# 작성자: 손삼주
# 작성일: 2026. 02. 20. 16:17:28

SELECT
    ANIMAL_ID,
    NAME,
    DATE_FORMAT(DATETIME, '%Y-%m-%d') as '날짜'
from ANIMAL_INS 
ORDER BY ANIMAL_ID