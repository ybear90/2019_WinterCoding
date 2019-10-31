"""
방법1: N이 상대적으로 작을 경우에 매우 효율적
복잡도 : O(N)
"""
def solution(n, lost, reserve):
    u = [1] * (n + 2) # 허깨비도 같이 세움(학생 index의 일관성 탐색을 위해)

    # reserve에 들어 있으면 ? 1로 증가
    for i in reserve:
        u[i] += 1
    # lost에 들어 있으면 ? 1을 감소시킴
    for i in lost:
        u[i] -= 1

    for i in range(1, n+1):
        # 앞사람에게 빌려줄 경우의 조건 체크(앞사람에게 빌려 주는 것을 우선)
        if u[i-1] == 0 and u[i] == 2:
            u[i-1:i+1] = [1, 1] # i-1 번째와 i를 둘다 1로 변경
        # 앞사람에게 빌려줄 필요 없이 뒷사람에게 빌려줄 경우
        elif u[i] == 2 and u[i+1] == 0:
            u[i:i+2] = [1, 1]

    return len([x for x in u[1:-1] if x > 0])

print(solution(5, [2, 4], [1, 3, 5])) # 5
print(solution(5, [2, 4], [3])) # 4
print(solution(3, [3], [1])) # 2
print(solution(5, [2, 3, 4], [2, 3, 4])) # 5