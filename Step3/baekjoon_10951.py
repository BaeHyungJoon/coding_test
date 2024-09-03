# 문제
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

# 입력
# 입력은 여러 개의 테스트 케이스로 이루어져 있다.

# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

# 출력
# 각 테스트 케이스마다 A+B를 출력한다.


# EOF (End of File) 개념을 알고 있어야 한다.
# sys 모듈을 사용할 줄 알아야 했다.
# sys.stdin 함수를 사용하자. -> 파일이 끝날때까지 계속 입력을 받을 수 있음.
import sys
for line in sys.stdin:
    A,B = map(int, line.split())
    print(A+B)