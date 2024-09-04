# 문제
# 총 N개의 정수가 주어졌을 때, 정수 v가 몇 개인지 구하는 프로그램을 작성하시오.
def find(n, lst, v):
    count = 0
    for i in range(n):
        if lst[i] == v:
            count += 1
    return count

# 입력
# 첫째 줄에 정수의 개수 N(1 ≤ N ≤ 100)이 주어진다. 
n = int(input())

# 둘째 줄에는 정수가 공백으로 구분되어져있다. 
lst = list(map(int, input().split()))

# 셋째 줄에는 찾으려고 하는 정수 v가 주어진다. 입력으로 주어지는 정수와 v는 -100보다 크거나 같으며, 100보다 작거나 같다.
v = int(input())

# 출력
# 첫째 줄에 입력으로 주어진 N개의 정수 중에 v가 몇 개인지 출력한다.
print(find(n, lst, v))