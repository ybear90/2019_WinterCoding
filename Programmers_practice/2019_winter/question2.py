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
