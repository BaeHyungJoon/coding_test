# 문제
# 어떤 숫자 n이 자신을 제외한 모든 약수들의 합과 같으면, 그 수를 완전수라고 한다.
# 예를 들어 6은 6 = 1 + 2 + 3 으로 완전수이다.
# n이 완전수인지 아닌지 판단해주는 프로그램을 작성하라.
def hyperfect_number(n):

    divisor_list = []
    for num in range(1, n):
        if n % num == 0:
            divisor_list.append(num)

    if sum(divisor_list) == n:
        print(n, '=', " + ".join(list(map(str,divisor_list))))
    else:
        print(f'{n} is NOT perfect.')

# 입력
# 입력은 테스트 케이스마다 한 줄 간격으로 n이 주어진다. (2 < n < 100,000)
# 입력의 마지막엔 -1이 주어진다.
inputs = []
while True:
    n = int(input())
    if n == -1:
        break
    inputs.append(n)

for i in inputs:
    hyperfect_number(i)

# 출력
# 테스트케이스 마다 한줄에 하나씩 출력해야 한다.
# n이 완전수라면, n을 n이 아닌 약수들의 합으로 나타내어 출력한다(예제 출력 참고).
# 이때, 약수들은 오름차순으로 나열해야 한다.
# n이 완전수가 아니라면 n is NOT perfect. 를 출력한다.