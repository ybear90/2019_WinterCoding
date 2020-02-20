"""
출처 : https://itholic.github.io/python-bfs-dfs/
"""

graph = {
    'A': ['B'],
    'B': ['A', 'C', 'H'],
    'C': ['B', 'D', 'G'],
    'D': ['C', 'E'],
    'E': ['D', 'F'],
    'F': ['E'],
    'G': ['D'],
    'H': ['B', 'I', 'J', 'M'],
    'I': ['H'],
    'J': ['H', 'K'],
    'K': ['J', 'L'],
    'L': ['K'],
    'M': ['H']
}

# def bfs(graph, start_node):
#     visit = list()
#     queue = list()
#
#     queue.append(start_node)
#
#     while queue:
#         node = queue.pop(0)
#         if node not in visit:
#             visit.append(node)
#             queue.extend(graph[node])
#         print("current queue: ", queue, "current visit: ", visit)
#
#     return visit



# print(bfs(graph, 'A'))

def dfs(graph, start_node):
    visit = list()
    stack = list()

    stack.append(start_node)
    while stack:
        print("current stack: ", stack)
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(graph[node])
        print("current visit: ", visit)

    return visit

print(dfs(graph, 'A'))
