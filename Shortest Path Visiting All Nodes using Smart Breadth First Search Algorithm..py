class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        goal = (1 << n) - 1
        queue = collections.deque((x, 1 << x) for x in range(n))
        steps = collections.defaultdict(lambda: n * n)
        for i in range(0, n):
            steps[i, 1 << i] = 0

        while queue:
            current_node, current_path = queue.popleft()
            current_steps = steps[current_node, current_path]
            if current_path == goal:
                return current_steps

            for child in graph[current_node]:
                child_steps = current_path | (1 << child)
                if steps[child, child_steps] > current_steps + 1:
                    steps[child, child_steps] = current_steps + 1
                    queue.append((child, child_steps))








