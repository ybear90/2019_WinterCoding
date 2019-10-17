def solution(answers):
    score_dict = dict()
    best_list = []

    for i in range(1, 4):
        score_dict[i] = 0

    giver1 = [1, 2, 3, 4, 5]
    giver2 = [2, 1, 2, 3, 2, 4, 2, 5]
    giver3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    # check giver the score
    for i in range(len(answers)):
        if answers[i] == giver1[i % len(giver1)]:
            score_dict[1] += 1
        if answers[i] == giver2[i % len(giver2)]:
            score_dict[2] += 1
        if answers[i] == giver3[i % len(giver3)]:
            score_dict[3] += 1

    # find maximum score
    maximum_score = max([i for i in score_dict.values()])

    # make best_list
    for key in score_dict.keys():
        if score_dict[key] == maximum_score:
            best_list.append(key)

    return best_list


print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))