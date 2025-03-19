import sys

from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end = ' ')

    for i in sorted(graph[v]):
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end = ' ')

        for i in sorted(graph[v]):
            if not visited[i]:
                queue.append(i) 
                visited[i] = True

n, m, v = map(int, sys.stdin.readline().split())
graph = dict()
for i in range(1, n + 1):
    graph[i] = []

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)



visited = [False] * (n + 1)
dfs(graph, v, visited)

print()

visited = [False] * (n + 1)
bfs(graph, v, visited)
    