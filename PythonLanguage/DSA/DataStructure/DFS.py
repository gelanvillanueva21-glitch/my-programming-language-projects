def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    result = [node]
    for neighbor in graph[node]:
        if neighbor not in visited:
            print(result)
            result += dfs(graph, neighbor, visited)
    return result


def dfs_iterative(graph, start):
    visited = set()
    stack   = [start]
    result  = []
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            result.append(node)
            for nb in reversed(graph[node]):
                if nb not in visited:
                    stack.append(nb)
        print(result)
    return result

social_network = {
    'Alice':  ['Bob', 'Charlie'],
    'Bob':    ['David', 'Eve'],
    'Charlie':['Eve'],
    'David':  [],
    'Eve':    ['Frank'],
    'Frank':  []
}
dfs_iterative(social_network, "Alice")