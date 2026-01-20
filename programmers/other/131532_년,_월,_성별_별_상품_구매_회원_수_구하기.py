# 년, 월, 성별 별 상품 구매 회원 수 구하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131532
# 작성자: 손삼주
# 작성일: 2026. 01. 20. 22:04:08

-- 코드를 입력하세요
SELECT
    YEAR(SALES_DATE) AS YEAR,
    MONTH(SALES_DATE) AS MONTH,
    GENDER,
    COUNT(DISTINCT O.USER_ID) AS USERS
FROM ONLINE_SALE O INNER JOIN 
    (SELECT *
     FROM USER_INFO 
     WHERE GENDER IS NOT NULL) AS U
    ON O.USER_ID = U.USER_ID
GROUP BY 1,2,3
ORDER BY 1,2,3