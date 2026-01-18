# 나머지 구하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120810
# 알고리즘: 기초
# 작성자: 손삼주
# 작성일: 2026. 01. 19. 01:25:07

def solution(num1, num2):
    if (num1/num2) <=0 or (num1/num2)>100:
        print("숫자를 다시 입력하세요.")
    else :
        result = num1 % num2
        return result