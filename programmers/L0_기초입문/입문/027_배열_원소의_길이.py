# 배열 원소의 길이
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120854
# 알고리즘: 기초
# 작성자: 손삼주
# 작성일: 2026. 03. 12. 15:55:38

def solution(strlist):
    answer = []
    for str in strlist:
        length = len(str)
        answer.append(length)
    return answer