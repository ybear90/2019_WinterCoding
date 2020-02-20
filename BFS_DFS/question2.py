"""
네트워크
"""
# By using BFS
# Ref) https://oneshottenkill.tistory.com/584
def solution(n, computers):
    answer = 0
    queue = []
    visited = [False] * n

    for i, com in enumerate(computers):
        if not visited[i]:
            answer += 1
            queue.append(i)

            while queue:
                idx = queue.pop(0)
                for j, cm in enumerate(computers[idx]):
                    if cm and not visited[j]:
                        visited[j] = True
                        queue.append(j)

    return answer