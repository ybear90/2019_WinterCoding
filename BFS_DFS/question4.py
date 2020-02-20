def solution(tickets):
    # 경로를 저장하는 사전 정의
    routes = {}

    for t in tickets:
        # 도착 공항을 추가
        # 리스트 병합으로 갱신해 나간다 (default : 빈 리스트)
        routes[t[0]] = routes.get(t[0], []) + [t[1]]
    for r in routes:
        # 각 키에 해당하는 리스트를 꺼내어 역순정렬한다
        routes[r].sort(reverse=True)

    stack = ["ICN"] # ICN에서 무조건 출발하므로 초기화
    path = [] # 최종 경로 리스트 초기화

    # 스택을 다 소모할 때 까지 진행하는 로직
    while len(stack) > 0:
        top = stack[-1]
        if top not in routes or len(routes[top]) == 0:
            path.append(stack.pop())
        else:
            # 알파벳 순서로 진행하므로 마지막 원소
            stack.append(routes[top][-1])
            # 진행한 경로 제외하고 가능한 경로 갱신
            routes[top] = routes[top][:-1]
    print("path: ", path)
    print("path_rev: ", path[::-1])
    return path[::-1]

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))