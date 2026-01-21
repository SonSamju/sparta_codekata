# 주문량이 많은 아이스크림들 조회하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/133027
# 작성자: 손삼주
# 작성일: 2026. 01. 21. 11:09:39

-- 코드를 입력하세요
SELECT 
    F.FLAVOR
FROM FIRST_HALF F LEFT JOIN JULY J
    ON F.FLAVOR = J.FLAVOR
GROUP BY F.FLAVOR
ORDER BY (SUM(F.TOTAL_ORDER)+SUM(J.TOTAL_ORDER)) DESC
LIMIT 3