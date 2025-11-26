[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/Uvhxywdx)
# hw05 – Route Planner: Choose BFS or Dijkstra

## Story

You are writing a **route planner** for a fantasy adventure game.  
Sometimes all roads are the same (unweighted).  
Sometimes roads have **travel times** (weighted).

You must plan a helper function that, given a graph and a flag, will:

- Use **BFS** for unweighted maps.
- Use **Dijkstra** for weighted maps.
- Return a suitable path and cost.

This homework combines ideas from hw01–hw04.

---

## Task

Write a function:

```python
route_planner(graph, start, goal, weighted)
```

- If `weighted` is `False`:

    - `graph`: dict `node -> list of neighbors (unweighted)`.

    - Use BFS to find a shortest path in number of edges.

    - Return `(path, steps)` where:

        - `path` is a list from `start` to `goal`.

        - `steps` is the number of edges `(len(path) - 1)`.

- If `weighted` is `True`:

    - `graph`: dict `node -> list of (neighbor, weight)` with positive weights.
    - Use Dijkstra to find path with minimum total weight.
    - Return `(path, total_cost)`.

In both cases:

- If `start` or `goal` is not in `graph`, or `goal` is unreachable:

    - return `( [], None )`.

### Constraints

- Up to 200 nodes and 1000 edges.

- When `weighted` is `True`, all weights are positive integers.

- Expected time complexity:

- Unweighted: O(V + E) [BFS].

- Weighted: O((V + E) log V) [Dijkstra].

---

## 8 Steps of Coding – Minimal Prompts (hw05)

You should now drive all 8 Steps yourself:

1. Read and understand the two modes (unweighted vs weighted).

2. Re-phrase the problem in your own words.

3. Decide the interface and data structures.

4. Break the problem into two algorithm branches.

5. Write pseudocode for each branch (BFS and Dijkstra).
6. Implement both branches cleanly (helper functions are OK).

7. Debug by testing both unweighted and weighted graphs.

8. Reflect on when each algorithm is used and why.

---

## Hints
1. You may write helper functions inside `main.py`, e.g. `_bfs_shortest_path` and `_dijkstra_shortest_path`.

2. Keep return format consistent: `(path, cost)` where cost is `steps` for BFS and total weight for Dijkstra.

3. Avoid code duplication when possible, but correctness is more important.

---

## How to Run Tests

python -m pytest -q

---

## FAQ
Q1: How do I know which graph format to expect?
A1: Check the `weighted` flag. If `False`, neighbors are plain strings. If `True`, neighbors are `(neighbor, weight)` pairs.

Q2: What should the function return when `start == goal`?
A2: A path `[start]` and cost `0` in both modes.

Q3: What if `start` or `goal` is missing?
A3: Return `([], None)`.

Q4: What if there is no path?
A4: Return `([], None)`.

Q5: Do I need to worry about negative weights?
A5: No. All weights are positive when `weighted` is `True`.

Q6: How will this be graded?
A6: Tests will exercise both modes (unweighted and weighted) and both success and failure cases.

Q7: What are common mistakes?
A7: Mixing the two graph formats, forgetting to handle the `weighted` flag, and returning inconsistent result formats.