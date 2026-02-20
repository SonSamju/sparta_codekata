# 즐겨찾기가 가장 많은 식당 정보 출력하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131123
# 작성자: 손삼주
# 작성일: 2026. 02. 20. 18:20:53

select
    food_type,
    rest_id,
    rest_name,
    favorites
from (
select
    food_type,
    rest_id,
    rest_name,
    favorites,
    dense_rank() over (partition by food_type order by favorites desc) as rnk 
from rest_info
) as a
where rnk = 1
order by food_type desc