from collections import deque


class BFS:
    """
    Breadth First Search Solver

    Returns:
    - shortest path from start to goal
    - explored nodes
    """

    def __init__(self, maze):

        self.maze = maze

        self.rows = len(maze)
        self.cols = len(maze[0])

        self.start = (0, 0)
        self.goal = (self.rows - 1, self.cols - 1)

    # --------------------------------------------------
    # Get Valid Neighbours
    # --------------------------------------------------

    def get_neighbors(self, row, col):

        neighbors = []

        cell = self.maze[row][col]

        # Top
        if not cell["top"] and row > 0:
            neighbors.append((row - 1, col))

        # Bottom
        if not cell["bottom"] and row < self.rows - 1:
            neighbors.append((row + 1, col))

        # Left
        if not cell["left"] and col > 0:
            neighbors.append((row, col - 1))

        # Right
        if not cell["right"] and col < self.cols - 1:
            neighbors.append((row, col + 1))

        return neighbors

    # --------------------------------------------------
    # Solve Maze
    # --------------------------------------------------

    def solve(self):

        queue = deque()

        queue.append(self.start)

        visited = set()
        visited.add(self.start)

        parent = {}

        explored = []

        while queue:

            current = queue.popleft()

            explored.append(current)

            if current == self.goal:
                break

            row, col = current

            for neighbor in self.get_neighbors(row, col):

                if neighbor not in visited:

                    visited.add(neighbor)

                    parent[neighbor] = current

                    queue.append(neighbor)

        # ----------------------------------------------
        # Reconstruct Path
        # ----------------------------------------------

        path = []

        if self.goal in parent or self.goal == self.start:

            current = self.goal

            while current != self.start:

                path.append(current)

                current = parent[current]

            path.append(self.start)

            path.reverse()

        return path, explored