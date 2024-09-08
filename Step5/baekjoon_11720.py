# 문제
# N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.
def add(n, number):
    sum = 0
    for i in range(n):
        sum += int(number[i])
    return sum

# 입력
# 첫째 줄에 숫자의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄에 숫자 N개가 공백없이 주어진다.
n = int(input())
number = input()

# 출력
# 입력으로 주어진 숫자 N개의 합을 출력한다.
print(add(n, number))