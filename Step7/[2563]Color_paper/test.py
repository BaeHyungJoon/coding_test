# 색종이의 좌표 리스트
x_list = []
y_list = []

# 색종이의 개수 입력
n = int(input())

# 색종이의 좌표 입력
for _ in range(n):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

# 총 넓이를 저장하는 변수
total_area = 0

# 각 색종이는 10x10의 크기를 가지므로 기본 넓이는 100
paper_size = 10 * 10

# 겹치는 영역을 확인할 함수
def check_overlap(x1, y1, x2, y2):
    x_overlap = max(0, min(x1 + 10, x2 + 10) - max(x1, x2))  # x축 겹침 구간 길이
    y_overlap = max(0, min(y1 + 10, y2 + 10) - max(y1, y2))  # y축 겹침 구간 길이
    return x_overlap * y_overlap  # 겹치는 넓이

# 모든 색종이에 대해 넓이를 더해나감
for i in range(n):
    total_area += paper_size  # 기본 색종이 넓이 추가
    for j in range(i):
        # 색종이 i와 j가 겹치는 경우, 겹치는 넓이를 빼줌
        overlap_area = check_overlap(x_list[i], y_list[i], x_list[j], y_list[j])
        total_area -= overlap_area

# 결과 출력
print(total_area)