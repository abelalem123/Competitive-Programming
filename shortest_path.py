from collections import defaultdict,deque
def shortestPath():
    graph = defaultdict(list)
    nodes, edges = map(int, input().split())
    source, target = map(int, input().split())
    visited = {source: -1}
    queue = deque([source])
    answer = []

    for _ in range(edges):
        node1, node2 = map(int, input().split())
        graph[node1].append(node2)
        graph[node2].append(node1)

    while  queue:
        node = queue.popleft()
        if node == target:
            break

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited[neighbour] = node
                queue.append(neighbour)
    if target not in visited:
        print(-1)
        return

    current = target
    while current != -1:
        answer.append(current)
        current = visited[current]

    print(len(answer) - 1)
    print(*answer[::-1])
shortestPath()
