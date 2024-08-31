#문제
#(세 자리 수) × (세 자리 수)는 다음과 같은 과정을 통하여 이루어진다.
#(1)과 (2)위치에 들어갈 세 자리 자연수가 주어질 때 (3), (4), (5), (6)위치에 들어갈 값을 구하는 프로그램을 작성하시오.

#입력
#첫째 줄에 (1)의 위치에 들어갈 세 자리 자연수가, 둘째 줄에 (2)의 위치에 들어갈 세자리 자연수가 주어진다.

#출력
#첫째 줄부터 넷째 줄까지 차례대로 (3), (4), (5), (6)에 들어갈 값을 출력한다.

def calculator(a, num):
    # a값을 num에 있는 숫자와 한번씩은 곱하고 그 결과들을 순서대로 출력해야 한다.
    result = list(map(lambda x : x * a, num))
    sum = 0
    for j in result:
        print(j)
    for k in range(len(result)):
        result[k] *= 10**k
    for l in result:
        sum += l
    print(sum)
    # result 내부에 있는 값
    

a = int(input())
# 문자열로 입력 받아서 리스트에 하나씩 숫자로 저장하기
b = input()
num = []

for i in range(len(b)):
    num.append(int(b[i]))

num.reverse()

calculator(a, num)