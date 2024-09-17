# 문제
# 가로, 세로의 크기가 각각 100인 정사각형 모양의 흰색 도화지가 있다. 
# 이 도화지 위에 가로, 세로의 크기가 각각 10인 정사각형 모양의 검은색 색종이를 색종이의 변과 도화지의 변이 평행하도록 붙인다. 
# 이러한 방식으로 색종이를 한 장 또는 여러 장 붙인 후 색종이가 붙은 검은 영역의 넓이를 구하는 프로그램을 작성하시오.

# 예를 들어 흰색 도화지 위에 세 장의 검은색 색종이를 그림과 같은 모양으로 붙였다면 검은색 영역의 넓이는 260이 된다.

def black_region(n, pos_list):

    # 겹치는 부분을 확인하거나, 전체 넓이에서 색종이 부분을 바꿔서 저장하고 마지막에 그 부분만 계산
    total_region = [[0] * 100 for _ in range(100)]

    for i in range(n):
        left = pos_list[i][0]
        bottom = pos_list[i][1]
        right = left + 10
        top = bottom + 10
        for j in range(left, right):
            for k in range(bottom, top):
                total_region[j][k] = 1

    region = sum(sum(row) for row in total_region)

    return region



# 입력
# 첫째 줄에 색종이의 수가 주어진다. 
n = int(input())
# 이어 둘째 줄부터 한 줄에 하나씩 색종이를 붙인 위치가 주어진다. 
# 색종이를 붙인 위치는 두 개의 자연수로 주어지는데 첫 번째 자연수는 색종이의 왼쪽 변과 도화지의 왼쪽 변 사이의 거리이고, 두 번째 자연수는 색종이의 아래쪽 변과 도화지의 아래쪽 변 사이의 거리이다. 
# 색종이의 수는 100 이하이며, 색종이가 도화지 밖으로 나가는 경우는 없다
pos_list = [list(map(int, input().split())) for _ in range(n)]

# 출력
# 첫째 줄에 색종이가 붙은 검은 영역의 넓이를 출력한다.
print(black_region(n, pos_list))