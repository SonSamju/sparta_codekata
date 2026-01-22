# 피자 나눠 먹기 (1)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120814
# 알고리즘: 기초
# 작성자: 손삼주
# 작성일: 2026. 01. 22. 09:09:37

def solution(n):
    if divmod(n,7)[1] != 0:
        answer = divmod(n,7)[0] + 1
    else:
        answer = divmod(n,7)[0]
    return answer