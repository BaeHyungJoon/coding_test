def triangle(a, b, c):

    what_triangle = ''
    if a == 60 and b == 60 and c == 60:
        what_triangle = 'Equilateral'
    elif a+b+c == 180:
        if (a==b or b==c or c==a):
            what_triangle = 'Isosceles'
        elif (a!=b and b!=c and c!=a):
            what_triangle = 'Scalene'
    elif a+b+c != 180:
        what_triangle = 'Error'
    
    return what_triangle


# 입력
# 총 3개의 줄에 걸쳐 삼각형의 각의 크기가 주어진다. 모든 정수는 0보다 크고, 180보다 작다.
a = int(input())
b = int(input())
c = int(input())

# 출력
# 문제의 설명에 따라 Equilateral, Isosceles, Scalene, Error 중 하나를 출력한다.
print(triangle(a,b,c))