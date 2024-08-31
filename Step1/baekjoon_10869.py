# 입력
# 두 자연수 A와 B가 주어진다. (1 ≤ A, B ≤ 10,000)

# 출력
# 첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다.

def operating(a, b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a//b)
    print(a%b)


a, b = map(int, input().split())
operating(a,b)