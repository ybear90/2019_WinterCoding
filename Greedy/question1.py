def solution(n, lost, reserve):
    # check duplicate elements
    duplicate_list = list(set(lost) & set(reserve))

    # remove duplicate elements
    for dup in duplicate_list:
        lost.remove(dup)
        reserve.remove(dup)

    # print("lost: ", lost, "reserve: ", reserve)

    possible = n - len(lost)


    while len(lost) > 0 and len(reserve) > 0:
        pop_lost = lost[0]
        # 수가 한없이 커질 때 불필요한 팀색을 진행함
        # 이 로직의 복잡도는 O(N^2) -> O(N) 이나 O(NlgN)으로 줄여야 효율성에서 안정적
        # for i in range(len(reserve)):
        #     if abs(pop_lost - reserve[i]) == 1:
        #         possible += 1
        #         reserve.pop(i)
        #         break
        # 동영상 강의 참조하여 O(N)으로 줄임
        if pop_lost + 1 in reserve:
            possible += 1
            reserve.remove(pop_lost+1)
        elif pop_lost - 1 in reserve:
            possible += 1
            reserve.remove(pop_lost-1)

        lost.pop(0)

    return possible

print(solution(5, [2, 4], [1, 3, 5])) # 5
print(solution(5, [2, 4], [3])) # 4
print(solution(3, [3], [1])) # 2
print(solution(5, [2, 3, 4], [2, 3, 4])) # 5
