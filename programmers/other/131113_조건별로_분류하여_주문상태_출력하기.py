# 조건별로 분류하여 주문상태 출력하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131113
# 작성자: 손삼주
# 작성일: 2026. 02. 20. 18:04:54

SELECT
    ORDER_ID,
    PRODUCT_ID,
    DATE_FORMAT(OUT_DATE, '%Y-%m-%d') as OUT_DATE,
    CASE WHEN OUT_DATE <= '2022-05-01' THEN '출고완료'
         WHEN OUT_DATE > '2022-05-01' THEN '출고대기'
         WHEN OUT_DATE IS NULL THEN '출고미정'
         END AS '출고여부'
FROM FOOD_ORDER
ORDER BY ORDER_ID ASC