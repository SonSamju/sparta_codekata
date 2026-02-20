# 조건에 맞는 사용자와 총 거래금액 조회하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/164668
# 작성자: 손삼주
# 작성일: 2026. 02. 20. 18:13:11

select
    user_id,
    nickname,
    sum(b.price) as total_sales
from used_goods_board b left join used_goods_user u
    on b.writer_id = u.user_id
where b.status = 'done'
group by b.writer_id
having sum(b.price) >= 700000
order by total_sales asc