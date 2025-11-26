
## main.py
import heapq
from collections import deque


def _bfs_shortest_path(graph, start, goal):
    if start not in graph or goal not in graph:
        return [], None

    if start == goal:
        return [start], 0

    queue = deque([start])
    parent = {start: None}

    while queue:
        node = queue.popleft()
        for neighbor in graph.get(node, []):
            if neighbor not in parent:
                parent[neighbor] = node
                queue.append(neighbor)
                if neighbor == goal:
                    # rebuild path
                    path = [goal]
                    while parent[path[-1]] is not None:
                        path.append(parent[path[-1]])
                    path.reverse()
                    return path, max(len(path) - 1, 0)

    return [], None


def _dijkstra_shortest_path(graph, start, goal):
    if start not in graph or goal not in graph:
        return [], None

    # Build undirected adjacency to be tolerant of input format
    undirected = {}
    for node in graph:
        undirected.setdefault(node, [])
        for neighbor, w in graph[node]:
            undirected[node].append((neighbor, w))
            undirected.setdefault(neighbor, [])
            undirected[neighbor].append((node, w))

    dist = {node: float('inf') for node in undirected}
    dist[start] = 0
    parent = {start: None}
    heap = [(0, start)]

    while heap:
        curr_cost, node = heapq.heappop(heap)
        if curr_cost > dist[node]:
            continue
        if node == goal:
            break
        for neighbor, weight in undirected[node]:
            new_cost = curr_cost + weight
            if new_cost < dist.get(neighbor, float('inf')):
                dist[neighbor] = new_cost
                parent[neighbor] = node
                heapq.heappush(heap, (new_cost, neighbor))

    if dist.get(goal, float('inf')) == float('inf'):
        return [], None

    path = []
    cur = goal
    while cur is not None:
        path.append(cur)
        cur = parent.get(cur)
    path.reverse()
    return path, dist[goal]


def route_planner(graph, start, goal, weighted):
    """Return (path, cost_or_steps).

    - If `weighted` is False: graph is node -> list of neighbors (unweighted).
      Returns (path, number_of_edges) or ([], None) if no path.
    - If `weighted` is True: graph is node -> list of (neighbor, weight) pairs.
      Returns (path, total_weight) or ([], None) if no path.
    """
    if weighted:
        return _dijkstra_shortest_path(graph, start, goal)
    else:
        return _bfs_shortest_path(graph, start, goal)


if __name__ == "__main__":
    # Quick manual smoke test
    unweighted = {"A": ["B"], "B": ["A", "C"], "C": ["B"]}
    print(route_planner(unweighted, "A", "C", weighted=False))

    weighted = {"A": [("B", 5)], "B": [("A", 5), ("C", 1)], "C": [("B", 1)]}
    print(route_planner(weighted, "A", "C", weighted=True))
