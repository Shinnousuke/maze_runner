
import cv2
import numpy as np


class MazeDrawer:
    """
    Draws the maze, player, explored nodes and solution path.
    """

    def __init__(
        self,
        maze,
        cell_size=40,
        player=None,
        path=None,
        explored=None
    ):

        self.maze = maze
        self.cell_size = cell_size
        self.player = player
        self.path = path
        self.explored = explored

        self.rows = len(maze)
        self.cols = len(maze[0])

        self.width = self.cols * cell_size
        self.height = self.rows * cell_size

    # -------------------------------------------------

    def draw(self):

        image = np.ones(
            (self.height + 1, self.width + 1, 3),
            dtype=np.uint8
        ) * 255

        # -----------------------------
        # Draw Maze Walls
        # -----------------------------

        for row in range(self.rows):

            for col in range(self.cols):

                cell = self.maze[row][col]

                x = col * self.cell_size
                y = row * self.cell_size

                if cell["top"]:
                    cv2.line(image, (x, y),
                             (x + self.cell_size, y),
                             (0, 0, 0), 2)

                if cell["left"]:
                    cv2.line(image, (x, y),
                             (x, y + self.cell_size),
                             (0, 0, 0), 2)

                if cell["right"]:
                    cv2.line(image,
                             (x + self.cell_size, y),
                             (x + self.cell_size,
                              y + self.cell_size),
                             (0, 0, 0), 2)

                if cell["bottom"]:
                    cv2.line(image,
                             (x, y + self.cell_size),
                             (x + self.cell_size,
                              y + self.cell_size),
                             (0, 0, 0), 2)

        # -----------------------------
        # Start Cell
        # -----------------------------

        cv2.rectangle(
            image,
            (5, 5),
            (self.cell_size - 5, self.cell_size - 5),
            (0, 255, 0),
            -1
        )

        # -----------------------------
        # Goal
        # -----------------------------

        goal_x = (self.cols - 1) * self.cell_size + self.cell_size // 2
        goal_y = (self.rows - 1) * self.cell_size + self.cell_size // 2

        cv2.circle(
            image,
            (goal_x, goal_y),
            self.cell_size // 4,
            (0, 0, 255),
            -1
        )

        # -----------------------------
        # Explored Nodes
        # -----------------------------

        if self.explored is not None:

            for row, col in self.explored:

                cx = col * self.cell_size + self.cell_size // 2
                cy = row * self.cell_size + self.cell_size // 2

                cv2.circle(
                    image,
                    (cx, cy),
                    self.cell_size // 8,
                    (255, 150, 0),
                    -1
                )

        # -----------------------------
        # Final Path
        # -----------------------------

        if self.path is not None:

            for row, col in self.path:

                cx = col * self.cell_size + self.cell_size // 2
                cy = row * self.cell_size + self.cell_size // 2

                cv2.circle(
                    image,
                    (cx, cy),
                    self.cell_size // 6,
                    (255, 0, 255),
                    -1
                )

        # -----------------------------
        # Player
        # -----------------------------

        if self.player is not None:

            row, col = self.player.get_position()

            cx = col * self.cell_size + self.cell_size // 2
            cy = row * self.cell_size + self.cell_size // 2

            cv2.circle(
                image,
                (cx, cy),
                self.cell_size // 4,
                (255, 0, 0),
                -1
            )

        return image