# 문제
# X대학 M교수님은 프로그래밍 수업을 맡고 있다. 
# 교실엔 학생이 30명이 있는데, 학생 명부엔 각 학생별로 1번부터 30번까지 출석번호가 붙어 있다.
# 교수님이 내준 특별과제를 28명이 제출했는데, 그 중에서 제출 안 한 학생 2명의 출석번호를 구하는 프로그램을 작성하시오.
def miss_number(lst):
    # 1차 구현
    # total_lst = list(range(1, 31))
    # miss = []

    # for num in total_lst:
    #     if num in lst:
    #         pass
    #     if num not in lst:
    #         miss.append(num)
    # return miss

    # 2차 구현
    # set을 사용하면 두 집합 사이의 차이를 쉽게 구할 수 있음.
    total_set = set(range(1, 31))
    submitted_set = set(lst)

    missing = sorted(total_set - submitted_set)

    return missing

# 입력
# 입력은 총 28줄로 각 제출자(학생)의 출석번호 n(1 ≤ n ≤ 30)가 한 줄에 하나씩 주어진다. 출석번호에 중복은 없다.
lst = [int(input()) for _ in range(28)]

# 출력
# 출력은 2줄이다. 1번째 줄엔 제출하지 않은 학생의 출석번호 중 가장 작은 것을 출력하고, 2번째 줄에선 그 다음 출석번호를 출력한다.
print(miss_number(lst)[0])
print(miss_number(lst)[1])