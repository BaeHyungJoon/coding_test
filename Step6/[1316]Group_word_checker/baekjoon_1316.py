# 문제
# 그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 
# 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.
# 단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

# from collections import Counter

def group_word_check(word_lst):
    
    group_word_cnt = 0

    ### 1차 풀이 ###

    # 문자열의 각 문자들이 몇 번 등장했는지 개수 세고
    # 2번 이상 등장한 문자들 중에서 해당 문자가 포함된 index 값을 받아와서 그 차이가 1보다 클 경우

    #for word in word_lst:
    #    word_cnt = Counter(word)

        # 이렇게 되면 counter로 각 문자의 등장 횟수를 셀 수는 있으나, value 값이 1인 것들과 2 이상인 것들에 대해서 분리하기가 어려움...

    ### 2차 풀이 ###

    # 앞에서부터 이전 문자와 같은 것이 나오는지 파악
    # 이전에 한번 등장한 적이 있는지 확인

    # word list에서 word 하나씩 확인
    for word in word_lst:
        
        seen = []
        is_group_word = True
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
                    is_group_word = False
                    break

            seen.append(word[i-1])
        seen.append(word[-1])

        if is_group_word:
            group_word_cnt += 1

    return group_word_cnt

# 입력
# 첫째 줄에 단어의 개수 N이 들어온다. N은 100보다 작거나 같은 자연수이다. 
n = int(input())
# 둘째 줄부터 N개의 줄에 단어가 들어온다. 단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.
word_lst = [input() for _ in range(n)]

# 출력
# 첫째 줄에 그룹 단어의 개수를 출력한다.
print(group_word_check(word_lst))