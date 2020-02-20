"""
아래와 같이 5와 사칙연산만으로 12를 표현할 수 있습니다.

12 = 5 + 5 + (5 / 5) + (5 / 5)
12 = 55 / 5 + 5 / 5
12 = (55 + 5) / 5

5를 사용한 횟수는 각각 6,5,4 입니다. 그리고 이중 가장 작은 경우는 4입니다.
이처럼 숫자 N과 number가 주어질 때, N과 사칙연산만 사용해서 표현 할 수 있는 방법 중 N 사용횟수의 최솟값을 return 하도록 solution 함수를 작성하세요.

제한사항
N은 1 이상 9 이하입니다.
number는 1 이상 32,000 이하입니다.
수식에는 괄호와 사칙연산만 가능하며 나누기 연산에서 나머지는 무시합니다.
최솟값이 8보다 크면 -1을 return 합니다.
"""
def solution(N, number):
    # 집합 8개 초기화
    # 중복을 허용하지 않고 수를 모으기
    s = [set() for x in range(8)]

    # set list의 index가 0부터 시작하는 것과 별개로 1~8까지 진행하기 위해 enumerate start 값을 1로 설정
    # 설정한 값 만큼 N의 갯수가 늘어 각각의 초기 set 원소를 설정
    for i, x in enumerate(s, start=1):
        x.add(int(str(N) * i))
    print("current set: ", s)
    # 사실 상 1개일 때 연산을 할 필요가 없으므로 N의 갯수가 2개인 집합부터 따져줌
    # D.P 개념을 사용하여 부분 해를 알 때 전체 해를 구하는 방식으로 진행
    # 실제 i번째(i+1 갯수의 해집합)의 집합을 완성 할 때 j : 0(1개의 해집합) ~ i-1, i - j - 1: j와 연산될 부분 해 집합(대칭적)번째의 해집합을
    # 부분 해끼리 연산하여(사칙연산) 구한다. -> Dynamic Programming
    for i in range(1, len(s)):
        for j in range(i):
            for op1 in s[j]:
                for op2 in s[i-j-1]:
                    print("i: ", i, "j: ", j, "i - j - 1: ", i - j - 1)
                    print("current op1: ", op1, "current op2: ", op2)
                    s[i].add(op1 + op2)
                    s[i].add(op1 - op2)
                    s[i].add(op1 * op2)
                    if op2 != 0:
                        s[i].add(op1 / op2)
                    print("current set2: ", s)
        if number in s[i]:
            answer = i + 1
            break
    else:
        answer = -1

    return answer

print(solution(5, 12))
print(solution(2, 11))