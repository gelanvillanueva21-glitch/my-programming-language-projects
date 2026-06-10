from collections import deque 

def bfs(graph, start):
    visited = set()
    queue   = deque([start])
    visited.add(start)
    result  = []
    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
        print(node, "->")
    return result


def bfs_path(graph, start, end):
    queue = deque([[start]])
    visited = set([start])
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == end: return path
        for nb in graph[node]:
            if nb not in visited:
                visited.add(nb)
                queue.append(path + [nb])
        print(path, "->")
    return None


graph = {
    "A": ["B", "D"],
    "B": ["A", "C", "E"],
    "C": ["B", "F"],
    "D": ["A", "E"],
    "E": ["B", "D", "F"],
    "F": ["C", "E"]
}
bfs(graph, "A")
bfs_path(graph, "A", "F")