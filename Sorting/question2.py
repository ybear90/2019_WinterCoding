"""
0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고,

이중 가장 큰 수는 6210입니다.

0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때,

순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

* 제한 사항
numbers의 길이는 1 이상 100,000 이하입니다.

numbers의 원소는 0 이상 1,000 이하입니다.

정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.

"""

def solution(numbers):
    # 숫자 배열을 문자열 배열로 변환
    numbers = [str(x) for x in numbers]
    # print("numbers1: ", numbers)

    # 크게 만드는 원소 우선으로 정렬기준을 정하여 정렬함수를 리스트 적용
    numbers.sort(key=lambda x : (x * 4)[:4], reverse=True)
    # print("numbers2: ", numbers)

    # 0이 맨 처음 나오는 경우 -> 0 '한글자로 처리'
    # 이런 특수한 경우가 있을 수 있다 : ['0', '0'] -> 예외처리 안하면 '00'으로 나옴
    if numbers[0] == '0':
        answer = '0'
    else:
        answer = ''.join(numbers)

    return answer

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
print(solution([0, 0]))