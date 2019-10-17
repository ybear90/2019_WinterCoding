def solution(budgets, M):
    if sum(budgets) <= M:
        return max(budgets)

    left = 0
    right = M  # 가능한 최대 예산 한계치
    max_budget_total = 0  # 가능한 지방 예상 총합(최대 갱신)
    max_upper_budget = 0  # 구하고자 하는 지방 예산 상한액

    while left < right:
        # 경계 내에서 계산한 예산 총액
        mid = int((left + right) / 2)
        bound_total = sum(min(mid, budget) for budget in budgets)

        if bound_total > M:
            right = mid
        else:
            if max_budget_total < bound_total:
                max_budget_total, max_upper_budget = bound_total, mid
            # 상한보다 못미칠 때는 사용했던 mid 보다 최소 1 커야 한다.
            left = mid + 1

    return min(max(budgets), max_upper_budget)

print(solution([120, 110, 140, 150], 485))