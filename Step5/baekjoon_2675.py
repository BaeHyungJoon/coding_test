# 문제
# 문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오. 
# 즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다. S에는 QR Code "alphanumeric" 문자만 들어있다.
# QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.
def repeat_word (lst):
    # lst에서 반복 횟수와 문자열을 가져오기
    for i in range(len(lst)):
        R = int(lst[i][0])
        S = lst[i][1]
        
        # S 문자열의 각 문자들을 R번 반복하고 새로운 문자열을 만들어서 출력.
        # 1차 풀이 : 빈 문자열을 생성 / S 문자열을 반복문으로 돌면서 R과 곱하기 / 빈 문자열에 문자를 집어넣기
        P = ""
        for j in S:
            P += j * R
        print(P)     


# 입력
# 첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 각 테스트 케이스는 반복 횟수 R(1 ≤ R ≤ 8), 문자열 S가 공백으로 구분되어 주어진다. S의 길이는 적어도 1이며, 20글자를 넘지 않는다. 
T = int(input())
lst = [list(map(str, input().split())) for _ in range(T)]

# 출력
# 각 테스트 케이스에 대해 P를 출력한다.
repeat_word(lst)