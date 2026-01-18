# 두 수의 나눗셈
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120806
# 알고리즘: 기초
# 작성자: 손삼주
# 작성일: 2026. 01. 19. 01:20:31

def solution(num1, num2):
    if 0 >= (num1/num2) or (num1/num2) >100:
        print("0보다 크고 100과 같거나 작은 값을 입력해주세요.")
    else:
        result = int(num1*1000/num2)
        return result