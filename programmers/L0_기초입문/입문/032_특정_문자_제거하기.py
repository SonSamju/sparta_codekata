# 특정 문자 제거하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120826
# 알고리즘: 기초
# 작성자: 손삼주
# 작성일: 2026. 03. 16. 21:26:09

def solution(my_string, letter):
    for i in letter:
        answer = my_string.replace(i,"")
    return answer