import math

def solution(progresses, speeds):
    day_list = []
    for p, s in zip(progresses, speeds):
        day_list.append(math.ceil((100 - p) / s))

    # find num of tasks
    answer = []
    count = 0

    while len(day_list) > 0:
        pop_data = day_list[0]

        while len(day_list) > 0:
            if pop_data >= day_list[0]:
                day_list.pop(0)
                count += 1
            else:
                break

        answer.append(count)
        count = 0

    return answer

print(solution([93, 30, 55], [1, 30, 5]))