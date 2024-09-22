# 문제
# 세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.
def find_fourth_point(point_list):


    if point_list[0][0] == point_list[1][0]:
        row = point_list[2][0]
    elif point_list[0][0] == point_list[2][0]:
        row = point_list[1][0]
    else:
        row = point_list[0][0]

    if point_list[0][1] == point_list[1][1]:
        column = point_list[2][1]
    elif point_list[0][1] == point_list[2][1]:
        column = point_list[1][1]
    else:
        column = point_list[0][1]

    print(row, column)

# 입력
# 세 점의 좌표가 한 줄에 하나씩 주어진다. 좌표는 1보다 크거나 같고, 1000보다 작거나 같은 정수이다.
point_list = [list(map(int, input().split())) for _ in range(3)]

# 출력
# 직사각형의 네 번째 점의 좌표를 출력한다.
find_fourth_point(point_list)

# 간결화 코드
# def find_fourth_point(points):
#     x_coords = [p[0] for p in points]
#     y_coords = [p[1] for p in points]

#     # x좌표 중 한 번만 등장한 값 찾기
#     x4 = min(x_coords, key=x_coords.count)
#     # y좌표 중 한 번만 등장한 값 찾기
#     y4 = min(y_coords, key=y_coords.count)

#     return x4, y4

# # 입력값
# points = [tuple(map(int, input().split())) for _ in range(3)]

# # 출력
# x4, y4 = find_fourth_point(points)
# print(x4, y4)