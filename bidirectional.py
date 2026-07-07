from collections import deque


class BidirectionalSearch:

    def __init__(self, maze):

        self.maze = maze
        self.rows = len(maze)
        self.cols = len(maze[0])

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

    def build_path(self, meet, parent_start, parent_goal):

        path1 = []

        node = meet

        while node is not None:
            path1.append(node)
            node = parent_start[node]

        path1.reverse()

        path2 = []

        node = parent_goal[meet]

        while node is not None:
            path2.append(node)
            node = parent_goal[node]

        return path1 + path2

    # -------------------------------------------------

    def solve(self):

        start = (0, 0)
        goal = (self.rows - 1, self.cols - 1)

        if start == goal:
            return [start], [start]

        queue_start = deque([start])
        queue_goal = deque([goal])

        visited_start = {start}
        visited_goal = {goal}

        parent_start = {start: None}
        parent_goal = {goal: None}

        explored = []

        while queue_start and queue_goal:

            # -----------------------------
            # Expand from Start
            # -----------------------------

            current = queue_start.popleft()
            explored.append(current)

            for neighbor in self.get_neighbors(*current):

                if neighbor not in visited_start:

                    visited_start.add(neighbor)
                    parent_start[neighbor] = current
                    queue_start.append(neighbor)

                    if neighbor in visited_goal:

                        path = self.build_path(
                            neighbor,
                            parent_start,
                            parent_goal
                        )

                        return path, explored

            # -----------------------------
            # Expand from Goal
            # -----------------------------

            current = queue_goal.popleft()
            explored.append(current)

            for neighbor in self.get_neighbors(*current):

                if neighbor not in visited_goal:

                    visited_goal.add(neighbor)
                    parent_goal[neighbor] = current
                    queue_goal.append(neighbor)

                    if neighbor in visited_start:

                        path = self.build_path(
                            neighbor,
                            parent_start,
                            parent_goal
                        )

                        return path, explored

        return [], explored