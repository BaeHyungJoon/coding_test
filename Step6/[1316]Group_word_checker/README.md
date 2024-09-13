# [백준 1316] 그룹 단어 체커

### 문제 링크
https://www.acmicpc.net/problem/1316

### 결과
#### <1차 풀이>
풀이 시간 : 20분

풀이 결과 : 실패

#### <2차 풀이>
메모리 : 31120 KB, 시간 : 40ms

### 분류
* 구현
* 문자열

## 문제 설명
그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.

단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

### 입력
첫째 줄에 단어의 개수 N이 들어온다. N은 100보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 단어가 들어온다. 단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.

### 출력
첫째 줄에 그룹 단어의 개수를 출력한다.  


## 초기 접근 방법 및 해결하지 못한 이유
### <1차 풀이 방법 생각>
* 주어진 단어 내부 문자들이 몇 번 등장했는지 개수를 센다.

* 그 중에서 2번 이상 등장한 문자들을 파악하고 해당 문자들의 처음과 끝 인덱스 값들을 받아와서 인덱스의 차가 1보다 크면 group 단어가 아니라고 판단한다.

#### 1차 작성한 코드
```python
from collections import Counter

def group_word_check(word_lst):

    group_word_cnt = 0

    for word in word_lst:
        word_cnt = Counter(word)
```

#### 1차 풀이 방법 포기 이유
* Counter 함수의 사용에 익숙하지 않았고, Counter로 얻어지는 dictionary의 사용이 익숙하지 않았다.

* 문자와 해당 문자가 등장한 횟수를 dict 형태로 반환하는데, 해당 dict value값 중에서 2 이상인 key 값들을 모으는 방법을 몰랐다.

* 만약 그렇게 2번 이상 등장한 문자들을 구한다고 해도, 이후에 반복문을 돌면서 문자열 내부 문자의 처음 등장 인덱스와 마지막 등장 인덱스를 하나씩 찾으려면 for문을 여러번 수행해야 한다.

### <2차 풀이 방법 생각>
* 문자열을 앞에서부터 바로 이전 문자와 같은지 확인한다.

* index 0번과 1번부터 비교하기 위해서 반복문의 시작을 1부터 시작하도록 설정

* word[i-1] 문자와 word[i]의 문자가 동일한지 조건문을 통해 확인하고, 동일하다면 탐색을 이어서 해야하므로 pass

* word[i-1] 문자와 word[i]의 문자가 다를 경우 그 word[i] 문자가 처음 나온 것인지, 아니면 이전에 나왔던 것인지 확인하는 것이 필요

* word[i]가 이전에 등장했다면 반복문을 종료하고 이전에 등장한 적이 없으면 그 이전의 문자 word[i-1]은 계속 같은 문자가 이어오다가 처음 끊긴 것이므로 이전에 등장한 문자들을 저장하는 리스트에 추가


#### 2차 작성한 코드
```python
def group_word_check(word_lst):

    group_word_cnt = 0

    for word in word_lst:
        seen = []
        # word의 문자 하나씩 탐색
        for i in range(1, len(word)):
            # 바로 이전 문자와 동일한지 확인
            # 동일한 경우에는 문제가 없으니 그대로 탐색 이어나가기
            if word[i-1] == word[i]:
                pass
            # 바로 이전 문자와 달라진 경우
            # 해당 문자가 이전에 등장한 적이 있는지 확인해야 함
            elif word[i-1] != word[i]:

                # 등장한 적이 있다면 group_word가 아니니 그만 탐색
                if word[i] in seen:
                    break
                # 등장한 적이 없다면 seen에 이전 문자를 넣고 이어서 탐색
                elif word[i] not in seen:
                    seen.append(word[i-1])
            group_word_cnt += 1

    return group_word_cnt
```
#### 2차 풀이 방법 문제 발생 이유
* group word인지 체크하는 것까지는 구현을 했으나, 이제 group word의 개수를 업데이트 하는 과정에서 문자를 하나씩 탐색하는 반복문 아래에 개수 업데이트 변수를 추가함

* 그러다보니 이전 문자와 동일할 경우에도 내려오면서 group_word_cnt를 업데이트하고 탐색이 모두 끝난 후에 최종 group word인지 판단하고 개수 업데이트를 하지 못하고 있음


## 해결 코드 및 방법
### <최종 코드>
```python
def group_word_check(word_lst):
    
    group_word_cnt = 0

    for word in word_lst:
        
        seen = []
        is_group_word = True

        for i in range(1, len(word)):

            if word[i-1] == word[i]:
                pass

            elif word[i-1] != word[i]:

                if word[i] in seen:
                    is_group_word = False
                    break

            seen.append(word[i-1])
        seen.append(word[-1])

        if is_group_word:
            group_word_cnt += 1

    return group_word_cnt


n = int(input())
word_lst = [input() for _ in range(n)]


print(group_word_check(word_lst))
```
### <해결 방법>
* group word인지 판단해주는 boolean 변수를 하나 설정

* 바로 이전 문자와 다를 경우에 해당 문자가 문자열에서 처음 등장하는 것이 아니라면 False를 가지고, 다른 문제가 없다면 True를 가지도록 설정

* 마지막에 해당 word의 문자열 탐색이 끝나면 is_group_word의 값이 True이면 group word의 개수를 업데이트



## 추가 공부
### GPT가 구현한 코드
```python
def is_group_word(word):
    seen = set()  # 이미 나온 문자를 기록할 집합
    prev_char = ''  # 이전 문자를 기록할 변수
    
    for char in word:
        if char != prev_char:
            if char in seen:
                return False  # 그룹 단어가 아님
            seen.add(char)  # 새 문자를 집합에 추가
        prev_char = char  # 현재 문자를 이전 문자로 설정
    
    return True  # 그룹 단어임

def count_group_words(words):
    return sum(1 for word in words if is_group_word(word))

# 입력 받기
n = int(input())
words = [input().strip() for _ in range(n)]

# 결과 출력
print(count_group_words(words))
```

* 전체적인 흐름은 비슷하다. 

    * 한번 나왔던 문자를 기록하는 공간을 set으로 사용한다.

        1. 탐색 효율성
            
            * list와 달리, set은 탐색 속도가 매우 빠릅니다. set의 탐색은 평균적으로 **O(1)**의 시간 복잡도를 가집니다. 이는 in 연산을 통해 문자가 set에 있는지 확인할 때, 고정된 시간 안에 처리가 가능하다는 의미입니다.

            * 반면, list는 **O(N)**의 시간 복잡도를 가집니다. 즉, 리스트에서 특정 문자가 있는지 확인하려면 리스트 전체를 순차적으로 탐색해야 하므로 단어가 길어질수록 속도가 느려집니다.

        2. 중복 허용하지 않음
            
            * set은 중복을 허용하지 않으므로, 이미 등장한 문자를 추가할 때 중복이 자동으로 제거됩니다. 예를 들어, 'a'라는 문자가 여러 번 등장하더라도 한 번만 저장되기 때문에 불필요한 중복을 처리할 필요가 없습니다.
    
    * 나는 리스트 slicing으로 이전문자와 현재문자의 동일 여부를 판단했다면, 여기서는 이전 문자를 기록할 변수를 하나 설정하고, for문을 돌면서 그룹단어인지 판단한 이후에 현재 문자를 이전 문자로 설정해주는 단계를 거친다.

