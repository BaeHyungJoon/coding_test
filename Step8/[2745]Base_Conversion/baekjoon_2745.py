# 문제
# B진법 수 N이 주어진다. 이 수를 10진법으로 바꿔 출력하는 프로그램을 작성하시오.
# 10진법을 넘어가는 진법은 숫자로 표시할 수 없는 자리가 있다. 이런 경우에는 다음과 같이 알파벳 대문자를 사용한다.
# A: 10, B: 11, ..., F: 15, ..., Y: 34, Z: 35
def decimal_number(n, b):
    # 10진법 수로 변경하려면 뒤에서부터 계산해야하기 때문에
    n = n[::-1]
    sum = 0
    b = int(b)

    number = {
        '0' : 0,
        '1' : 1,
        '2' : 2,
        '3' : 3,
        '4' : 4,
        '5' : 5,
        '6' : 6,
        '7' : 7,
        '8' : 8,
        '9' : 9,
        'A' : 10,
        'B' : 11,
        'C' : 12,
        'D' : 13,
        'E' : 14,
        'F' : 15,
        'G' : 16,
        'H' : 17,
        'I' : 18,
        'J' : 19,
        'K' : 20,
        'L' : 21,
        'M' : 22,
        'N' : 23,
        'O' : 24,
        'P' : 25,
        'Q' : 26,
        'R' : 27,
        'S' : 28,
        'T' : 29,
        'U' : 30,
        'V' : 31,
        'W' : 32,
        'X' : 33,
        'Y' : 34,
        'Z' : 35
    }

    a = ''
    for i in range(len(n)):
        sum += number[n[i]] * (b ** i)

    return sum

# 입력
# 첫째 줄에 N과 B가 주어진다. (2 ≤ B ≤ 36)
# B진법 수 N을 10진법으로 바꾸면, 항상 10억보다 작거나 같다.
N, B = map(str, input().split())

# 출력
# 첫째 줄에 B진법 수 N을 10진법으로 출력한다.
print(decimal_number(N,B))