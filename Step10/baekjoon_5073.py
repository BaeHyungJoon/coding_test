# 문제
# 삼각형의 세 변의 길이가 주어질 때 변의 길이에 따라 다음과 같이 정의한다.

# Equilateral :  세 변의 길이가 모두 같은 경우
# Isosceles : 두 변의 길이만 같은 경우
# Scalene : 세 변의 길이가 모두 다른 경우
# 단 주어진 세 변의 길이가 삼각형의 조건을 만족하지 못하는 경우에는 "Invalid" 를 출력한다. 예를 들어 6, 3, 2가 이 경우에 해당한다. 
# 가장 긴 변의 길이보다 나머지 두 변의 길이의 합이 길지 않으면 삼각형의 조건을 만족하지 못한다.

# 세 변의 길이가 주어질 때 위 정의에 따른 결과를 출력하시오.
def triangle(a, b, c):

    result = ''
    side = [a, b, c]
    max_side = max(side)

    side.remove(max(side))

    if sum(side) <= max_side:
        result = 'Invalid'
    else:

        if a == b and b == c and c == a:
            result = 'Equilateral'
        elif a == b or b == c or c == a:
            result = 'Isosceles'
        elif a!=b and b!=c and c!=a:
            result = 'Scalene'

    return result

# 입력
# 각 줄에는 1,000을 넘지 않는 양의 정수 3개가 입력된다. 마지막 줄은 0 0 0이며 이 줄은 계산하지 않는다.
decision = []

while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    else:
        decision.append(triangle(a,b,c))


# 출력
# 각 입력에 맞는 결과 (Equilateral, Isosceles, Scalene, Invalid) 를 출력하시오.
for output in decision:
    print(output)


# def classify_triangle(a, b, c):
#     sides = [a, b, c]
#     sides.sort()  # 오름차순 정렬하여 가장 긴 변이 맨 뒤에 오도록 함

#     # 삼각형이 성립하지 않는 경우
#     if sides[2] >= sides[0] + sides[1]:
#         return "Invalid"
    
#     # 세 변이 모두 같은 경우
#     if a == b == c:
#         return "Equilateral"
    
#     # 두 변이 같은 경우
#     if a == b or b == c or a == c:
#         return "Isosceles"
    
#     # 세 변이 모두 다른 경우
#     return "Scalene"

# while True:
#     a, b, c = map(int, input().split())
    
#     # 종료 조건
#     if a == 0 and b == 0 and c == 0:
#         break
    
#     # 삼각형 분류 출력
#     print(classify_triangle(a, b, c))