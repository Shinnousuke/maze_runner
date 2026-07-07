from collections import deque


class DFS:
    """
    Depth First Search Maze Solver
    """

    def __init__(self, maze):

        self.maze = maze
        self.rows = len(maze)
        self.cols = len(maze[0])

        self.start = (0, 0)
        self.goal = (self.rows - 1, self.cols - 1)

    # --------------------------------------------------

    def get_neighbors(self, row, col):

        neighbors = []

        cell = self.maze[row][col]

        # UP
        if not cell["top"] and row > 0:
            neighbors.append((row - 1, col))

        # DOWN
        if not cell["bottom"] and row < self.rows - 1:
            neighbors.append((row + 1, col))

        # LEFT
        if not cell["left"] and col > 0:
            neighbors.append((row, col - 1))

        # RIGHT
        if not cell["right"] and col < self.cols - 1:
            neighbors.append((row, col + 1))

        return neighbors

    # --------------------------------------------------

    def solve(self):

        stack = [self.start]

        visited = set()

        parent = {}

        explored = []

        while stack:

            current = stack.pop()

            if current in visited:
                continue

            visited.add(current)

            explored.append(current)

            if current == self.goal:
                break

            for neighbor in reversed(self.get_neighbors(*current)):

                if neighbor not in visited:

                    stack.append(neighbor)

                    if neighbor not in parent:
                        parent[neighbor] = current

        path = []

        node = self.goal

        while node != self.start:

            path.append(node)

            node = parent[node]

        path.append(self.start)

        path.reverse()

        return path, explored