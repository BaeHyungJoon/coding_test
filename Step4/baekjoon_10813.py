# 문제
# 도현이는 바구니를 총 N개 가지고 있고, 각각의 바구니에는 1번부터 N번까지 번호가 매겨져 있다. 
# 바구니에는 공이 1개씩 들어있고, 처음에는 바구니에 적혀있는 번호와 같은 번호가 적힌 공이 들어있다.
# 도현이는 앞으로 M번 공을 바꾸려고 한다. 도현이는 공을 바꿀 바구니 2개를 선택하고, 두 바구니에 들어있는 공을 서로 교환한다.
# 공을 어떻게 바꿀지가 주어졌을 때, M번 공을 바꾼 이후에 각 바구니에 어떤 공이 들어있는지 구하는 프로그램을 작성하시오.
def change(n, lst):
    # 바구니에는 공이 1개씩 들어있고, 처음에는 바구니에 적혀있는 번호와 같은 번호가 적힌 공이 들어있음.
    # basket = []
    # for k in range(n):
    #     basket.append(k+1)
    # 한번에 간단히 표기
    basket = list(range(1,n+1))

    # # 도현이는 공을 바꿀 바구니 2개를 선택하고, 두 바구니에 들어있는 공을 서로 교환
    # for num in range(len(lst)):
    #     i = lst[num][0]
    #     j = lst[num][1]

    #     tmp = basket[i-1]
    #     basket[i-1] = basket[j-1]
    #     basket[j-1] = tmp
    # python에서는 tuple을 사용하여 손쉽게 변환 가능
    for i,j in lst:
        basket[i-1], basket[j-1] = basket[j-1], basket[i-1]
    
    return basket
# 입력
# 첫째 줄에 N (1 ≤ N ≤ 100)과 M (1 ≤ M ≤ 100)이 주어진다.
# 둘째 줄부터 M개의 줄에 걸쳐서 공을 교환할 방법이 주어진다. 
# 각 방법은 두 정수 i j로 이루어져 있으며, i번 바구니와 j번 바구니에 들어있는 공을 교환한다는 뜻이다. (1 ≤ i ≤ j ≤ N)
# 도현이는 입력으로 주어진 순서대로 공을 교환한다.
n, m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(m)]

# 출력
# 1번 바구니부터 N번 바구니에 들어있는 공의 번호를 공백으로 구분해 출력한다.
print(' '.join(map(str,change(n, lst))))