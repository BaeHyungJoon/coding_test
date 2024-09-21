# 문제
# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.
def prime_number(n, num_list):

    # 소수인지 확인하는 방법
    # 소수 : 1과 자기 자신만을 약수로 가지는 수
    count = 0

    for i in range(n):
        lst = []
        for j in range(1, num_list[i] + 1):
            if num_list[i] % j == 0:
                lst.append(num_list[i])
        if len(lst) == 2:
            count += 1

    return count

# 입력
# 첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.
n = int(input())
num_list = list(map(int,input().split()))

# 출력
# 주어진 수들 중 소수의 개수를 출력한다.
print(prime_number(n, num_list))