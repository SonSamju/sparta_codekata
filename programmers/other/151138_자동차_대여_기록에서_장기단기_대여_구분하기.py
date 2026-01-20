# 자동차 대여 기록에서 장기/단기 대여 구분하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/151138
# 작성자: 손삼주
# 작성일: 2026. 01. 20. 22:34:12

-- 코드를 입력하세요
SELECT 
    HISTORY_ID, 
    CAR_ID, 
    DATE_FORMAT(START_DATE, '%Y-%m-%d') as START_DATE, 
    DATE_FORMAT(END_DATE, '%Y-%m-%d') as END_DATE,
    CASE WHEN DATEDIFF(END_DATE,START_DATE) + 1 >=30 THEN '장기 대여'
    ELSE '단기 대여' END AS RENT_TYPE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE START_DATE >= '2022-09-01' AND START_DATE <= '2022-09-30'
ORDER BY HISTORY_ID DESC