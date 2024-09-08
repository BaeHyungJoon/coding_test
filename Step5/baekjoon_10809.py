# 문제
# 알파벳 소문자로만 이루어진 단어 S가 주어진다. 
# 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.
def find_alphabet_position(word):
    # 알파벳 하나하나 if문을 돌릴 수는 없는 노릇...
    # 없는 알파벳을 -1로 지정하는 것보다 원래 -1로 두고 있는 것들을 바꾸는 게 더 나을듯
    alphabet = [-1] * 26

    # word 문자열을 반복문을 돌면서 문자와 문자의 문자열 내부 위치 정보를 저장
    for i, char in enumerate(word):
        alphabet_index = ord(char) - ord('a')
        if alphabet[alphabet_index] == -1:
            alphabet[alphabet_index] = i

    return alphabet

# 입력
# 첫째 줄에 단어 S가 주어진다. 단어의 길이는 100을 넘지 않으며, 알파벳 소문자로만 이루어져 있다.
word = input()

# 출력
# 각각의 알파벳에 대해서, a가 처음 등장하는 위치, b가 처음 등장하는 위치, ... z가 처음 등장하는 위치를 공백으로 구분해서 출력한다.
# 만약, 어떤 알파벳이 단어에 포함되어 있지 않다면 -1을 출력한다. 단어의 첫 번째 글자는 0번째 위치이고, 두 번째 글자는 1번째 위치이다.
position = find_alphabet_position(word)
print(*position)