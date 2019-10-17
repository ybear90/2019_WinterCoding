def solution(budgets, M):
    if sum(budgets) <= M:
        return max(budgets)

    budgets.sort()

    avrp_budget = M // len(budgets)
    # avr_budget = sum(budgets) // len(budgets)

    mid = (0 + len(budgets)) // 2
    start = mid

    # start index settings
    for i in range(mid, len(budgets)):
        if budgets[i] >= avrp_budget:
            start = i
            break
    for i in range(mid - 1, -1, -1):
        if budgets[i] >= avrp_budget:
            start = i

    for upper in range(avrp_budget, max(budgets)):
        # start index setting
        for idx in range(len(budgets) - 1, start - 1, -1):
            if upper > budgets[idx]:
                start = idx
                break

        reduce = M - sum(budgets[:start])
        for idx in range(start, len(budgets)):
            if budgets[idx] < upper:
                reduce -= budgets[idx]
                start = idx
                continue
            reduce -= upper
            if reduce <= 0 and idx < len(budgets):
                if reduce == 0 and idx == len(budgets) - 1:
                    return upper
                else:
                    return upper - 1