# 나이 출력
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120820
# 알고리즘: 기초
# 작성자: 손삼주
# 작성일: 2026. 01. 19. 01:07:59

def solution(age):
    if age < 0 or age > 120:
        print("나이는 1세이상 120세이하 값입니다.")
    else:
        birth_year = 2022-(age-1) 
        return birth_year