# 짝수 홀수 개수
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120824
# 알고리즘: 기초
# 작성자: 손삼주
# 작성일: 2026. 03. 16. 21:37:14

def solution(num_list):
    answer = []
    even_cnt = 0
    odd_cnt = 0
    for num in num_list:
        if num % 2 == 0:
            even_cnt += 1
        else:
            odd_cnt += 1
    answer.append(even_cnt)
    answer.append(odd_cnt)
    return answer