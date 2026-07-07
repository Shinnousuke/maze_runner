from heapq import heappush, heappop


class Greedy:

    def __init__(self, maze):

        self.maze = maze
        self.rows = len(maze)
        self.cols = len(maze[0])

    # -------------------------------------------------

    def heuristic(self, node):

        row, col = node

        goal = (self.rows - 1, self.cols - 1)

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
        heappush(frontier, (self.heuristic(start), start))

        parent = {}
        visited = {start}

        explored = []

        while frontier:

            _, current = heappop(frontier)

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

                if neighbor not in visited:

                    visited.add(neighbor)
                    parent[neighbor] = current

                    heappush(
                        frontier,
                        (self.heuristic(neighbor), neighbor)
                    )

        return [], explored