"""
# question 2 : 종이접기 문제(마루 골 문제)

시간이 없어서 직접 규칙성을 찾지는 못했지만

구글링을 하여 종이접기라고 검색 했을 때 마루 골이 생기는 규칙성이 나왔고 해당 규칙성을 토대로

코드 구현

"""

def solution(n):
    answer = []
    if n == 1:
        answer.append(0)
        return answer
    else:
        answer.append(0)
        for i in range(1, n):
            answer.insert(0, 0)
            before = [1 - x for x in answer[1:]]
            before.reverse()
            answer = before + answer
            a_idx = 0
            # for j in range(1, len(answer)):
            #     answer.insert(0, 1 - answer[a_idx+j])
            #     a_idx += 1
    answer.reverse()
    return answer

# print(solution(1))
# print(solution(2))
# print(solution(3))
# print(solution(4))
# print(solution(5))
print(solution(20))
