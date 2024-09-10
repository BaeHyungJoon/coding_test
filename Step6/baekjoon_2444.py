# 문제
# 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.
def print_star(N):
    # 상단 피라미드
    for i in range(1, N + 1):
        # 공백 출력: N-i 개
        print(' ' * (N - i), end='')
        # 별 출력: 2*i - 1 개
        print('*' * (2 * i - 1))
    
    # 하단 피라미드
    for i in range(N - 1, 0, -1):
        # 공백 출력: N-i 개
        print(' ' * (N - i), end='')
        # 별 출력: 2*i - 1 개
        print('*' * (2 * i - 1))

# 입력
# 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
n = int(input())

# 출력
# 첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.
print_star(n)
