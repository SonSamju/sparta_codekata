# 배열 뒤집기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120821
# 알고리즘: 기초
# 작성자: 손삼주
# 작성일: 2026. 01. 21. 20:50:26

def solution(num_list):
    answer = [i for i in num_list[::-1]]
    return answer