# 카테고리 별 상품 개수 구하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131529
# 작성자: 손삼주
# 작성일: 2026. 02. 20. 16:31:55

SELECT
    SUBSTR(PRODUCT_CODE,1,2) AS CATEGORY,
    COUNT(*) AS PRODUCTS
FROM PRODUCT
GROUP BY 1
ORDER BY PRODUCT_CODE