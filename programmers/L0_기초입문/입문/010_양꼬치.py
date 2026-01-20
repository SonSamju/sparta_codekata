# 양꼬치
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120830
# 알고리즘: 기초
# 작성자: 손삼주
# 작성일: 2026. 01. 20. 21:24:09

def solution(n, k):
    service = divmod(n,10)[0]
    total = n*12000 + (k-service)*2000
    return total