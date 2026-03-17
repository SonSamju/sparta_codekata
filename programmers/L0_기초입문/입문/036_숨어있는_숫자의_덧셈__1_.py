# 숨어있는 숫자의 덧셈 (1)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120851
# 알고리즘: 기초
# 작성자: 손삼주
# 작성일: 2026. 03. 17. 09:29:29

def solution(my_string):
    answer = 0
    for i in my_string:
        try:
            int(i)
            answer += int(i)
        except ValueError:
            continue
    return answer