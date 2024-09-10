# 문제
# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

# 주로 데이터의 빈도(count)를 계산하는 데 사용. iterable한 객체의 요소들이 각각 몇 번 등장했는지 셀 수 있음.
# 각 요소들은 딕셔너리의 키가 되고, 등장한 횟수가 value로 저장
from collections import Counter

def most_alphabet(word):
    # 알파벳 빈도 계산
    counter = Counter(word)

    # 가장 많이 사용된 알파벳의 빈도 추출
    max_count = max(counter.values())

    most_frequent = []
    for char, count in counter.items():
        if count == max_count:
            most_frequent.append(char)

    if len(most_frequent) > 1:
        return '?'
    else:
        return most_frequent[0]


# 입력
# 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.
word = input().upper()

# 출력
# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.
print(most_alphabet(word))