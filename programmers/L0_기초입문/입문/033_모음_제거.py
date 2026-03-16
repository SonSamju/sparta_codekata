# 모음 제거
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120849
# 알고리즘: 기초
# 작성자: 손삼주
# 작성일: 2026. 03. 16. 21:31:48

def solution(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    answer = my_string
    for vowel in vowels:
        if vowel in my_string:
            answer = answer.replace(vowel, '')
    return answer