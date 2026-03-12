# 아이스 아메리카노
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120819
# 알고리즘: 기초
# 작성자: 손삼주
# 작성일: 2026. 03. 12. 15:59:16

def solution(money):
    answer = []
    n, m = divmod(money, 5500)
    answer.append(n)
    answer.append(m)
    return answer