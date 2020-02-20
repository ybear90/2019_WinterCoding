def solution(array, commands):
    sorted_list = []
    answer_list = []

    # slicing & indexing
    for com in commands:
        sorted_list = sorted(array[com[0]-1:com[1]])
        answer_list.append(sorted_list[com[2]-1])

    return answer_list

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))