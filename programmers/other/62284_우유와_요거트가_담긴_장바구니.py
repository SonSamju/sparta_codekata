# 우유와 요거트가 담긴 장바구니
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/62284
# 작성자: 손삼주
# 작성일: 2026. 01. 21. 10:43:21

SELECT
    CART_ID
FROM CART_PRODUCTS
WHERE NAME IN ('MILK', 'YOGURT')
GROUP BY CART_ID
HAVING COUNT(DISTINCT NAME) >=2
ORDER BY CART_ID