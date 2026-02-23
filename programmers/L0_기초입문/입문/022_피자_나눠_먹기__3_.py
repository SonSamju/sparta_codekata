# 피자 나눠 먹기 (3)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120816
# 알고리즘: 기초
# 작성자: 손삼주
# 작성일: 2026. 02. 23. 13:19:08

def solution(slice, n):
    if slice >= n:
        answer = 1
    else:
        if n%slice ==0 :
            answer = (n/slice)
        else:
            answer = (n//slice +1)
    return answer