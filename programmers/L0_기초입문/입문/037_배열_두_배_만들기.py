# 배열 두 배 만들기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120809
# 알고리즘: 기초
# 작성자: 손삼주
# 작성일: 2026. 03. 17. 09:35:55

def solution(numbers):
    answer = numbers
    for i in range(len(numbers)):
        answer[i] = answer[i]*2
    return answer