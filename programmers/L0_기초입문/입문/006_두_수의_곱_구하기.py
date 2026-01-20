# 두 수의 곱 구하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120804
# 알고리즘: 기초
# 작성자: 손삼주
# 작성일: 2026. 01. 20. 20:53:39

def solution(num1, num2):
    if 0 <= num1 <= 100 and 0 <= num2 <= 100:
        answer = num1*num2
        return answer
    else : 
        print("숫자를 다시 입력하세요.")


# 다른 풀이방법

def solution(num1, num2):
    #return num1 * num2
    i = 0
    answer = 0
    while i < num2:
        answer += num1
        i += 1
    return answer

#while문을 사용해서 num1,num2 > 0 제한조건을 만족시킨 점이 신기했다.
