from heapq import heappush, heappop


class AStar:

    def __init__(self, maze):

        self.maze = maze
        self.rows = len(maze)
        self.cols = len(maze[0])

    # -------------------------------------------------

    def heuristic(self, node):

        row, col = node

        goal = (self.rows - 1, self.cols - 1)

        # Manhattan Distance
        return abs(row - goal[0]) + abs(col - goal[1])

    # -------------------------------------------------

    def get_neighbors(self, row, col):

        neighbors = []

        cell = self.maze[row][col]

        if not cell["top"] and row > 0:
            neighbors.append((row - 1, col))

        if not cell["bottom"] and row < self.rows - 1:
            neighbors.append((row + 1, col))

        if not cell["left"] and col > 0:
            neighbors.append((row, col - 1))

        if not cell["right"] and col < self.cols - 1:
            neighbors.append((row, col + 1))

        return neighbors

    # -------------------------------------------------

    def solve(self):

        start = (0, 0)
        goal = (self.rows - 1, self.cols - 1)

        frontier = []

        # (f = g+h, g, node)
        heappush(frontier, (self.heuristic(start), 0, start))

        parent = {}

        g_cost = {start: 0}

        explored = []

        while frontier:

            f, cost, current = heappop(frontier)

            if current in explored:
                continue

            explored.append(current)

            if current == goal:

                path = []

                while current != start:
                    path.append(current)
                    current = parent[current]

                path.append(start)
                path.reverse()

                return path, explored

            row, col = current

            for neighbor in self.get_neighbors(row, col):

                new_cost = cost + 1

                if neighbor not in g_cost or new_cost < g_cost[neighbor]:

                    g_cost[neighbor] = new_cost

                    priority = new_cost + self.heuristic(neighbor)

                    heappush(
                        frontier,
                        (priority, new_cost, neighbor)
                    )

                    parent[neighbor] = current

        return [], explored