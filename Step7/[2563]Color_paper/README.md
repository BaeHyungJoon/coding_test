# [백준 2563] 색종이

### 문제 링크
https://www.acmicpc.net/problem/2563

### 결과
#### <1차 풀이>
풀이 시간 : 20분

풀이 결과 : 실패

#### <2차 풀이>
메모리 : 31120 KB, 시간 : 36ms

### 분류
* 구현

## 문제 설명
가로, 세로의 크기가 각각 100인 정사각형 모양의 흰색 도화지가 있다. 이 도화지 위에 가로, 세로의 크기가 각각 10인 정사각형 모양의 검은색 색종이를 색종이의 변과 도화지의 변이 평행하도록 붙인다. 이러한 방식으로 색종이를 한 장 또는 여러 장 붙인 후 색종이가 붙은 검은 영역의 넓이를 구하는 프로그램을 작성하시오.

예를 들어 흰색 도화지 위에 세 장의 검은색 색종이를 그림과 같은 모양으로 붙였다면 검은색 영역의 넓이는 260이 된다.

### 입력
첫째 줄에 색종이의 수가 주어진다. 이어 둘째 줄부터 한 줄에 하나씩 색종이를 붙인 위치가 주어진다. 색종이를 붙인 위치는 두 개의 자연수로 주어지는데 첫 번째 자연수는 색종이의 왼쪽 변과 도화지의 왼쪽 변 사이의 거리이고, 두 번째 자연수는 색종이의 아래쪽 변과 도화지의 아래쪽 변 사이의 거리이다. 색종이의 수는 100 이하이며, 색종이가 도화지 밖으로 나가는 경우는 없다

### 출력
첫째 줄에 색종이가 붙은 검은 영역의 넓이를 출력한다. 


## 초기 접근 방법 및 해결하지 못한 이유
### <1차 풀이 방법 생각>
* 색종이의 전체 최대 넓이는 색종이의 개수 * 100

* 입력 받은 왼쪽과 아래쪽 위치의 값들을 리스트로 저장해서 리스트 내부의 원소들끼리의 차가 10보다 작은 경우 겹치는 종이가 발생한다고 판단

* 겹치는 부분을 전체 최대 넓이에서 빼주면 된다.

#### 1차 풀이 방법 포기 이유
* left, bottom 값을 list에 저장은 할 수 있는데, 그 이후에 left 리스트와 bottom 리스트에서 여러 원소들 중 차가 10 이하인 것들을 찾는 방법이 너무 복잡하다고 생각했다.

### <2차 풀이 방법 생각>
* 문제에서 전체 흰색 도화지가 가로 100, 세로 100 사이즈로 존재한다고 나와있다.

* 해당 도화지를 0으로 가득찬 2차원 배열로 생성한다.

* 색종이의 left, bottom 값을 가져와서 해당 넓이 부분을 1로 바꿔주는 작업을 반복한다.

* 겹치는 부분은 이미 1이기 때문에 덮어씌워지면서 중복된 부분이 자연스럽게 제거 된다.

* 마지막에는 각 행 별로 탐색하면서 list의 값들을 모두 더해서 최종 넓이를 구한다.

### <최종 코드>
```python
def black_region(n, pos_list):

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

# 입출력 단계
n = int(input())
pos_list = [list(map(int, input().split())) for _ in range(n)]

print(black_region(n, pos_list))
```

## 추가 공부
### GPT가 짠 코드
* 내가 초반에 고민했던 방법으로 GPT에게 코드 작성을 물어봤고, 다음과 같은 답변을 얻었다.

```python
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
```
