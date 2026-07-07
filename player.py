class Player:
    """
    Represents the player inside the maze.

    Responsibilities:
    - Store current position
    - Move if there is no wall
    - Check if goal is reached
    """

    def __init__(self, maze):

        self.maze = maze

        self.rows = len(maze)
        self.cols = len(maze[0])

        # Start position
        self.row = 0
        self.col = 0

        # Goal position
        self.goal_row = self.rows - 1
        self.goal_col = self.cols - 1

    # -----------------------------------------
    # Current Position
    # -----------------------------------------

    def get_position(self):
        return self.row, self.col

    # -----------------------------------------
    # Move Up
    # -----------------------------------------

    def move_up(self):

        cell = self.maze[self.row][self.col]

        if not cell["top"] and self.row > 0:
            self.row -= 1

    # -----------------------------------------
    # Move Down
    # -----------------------------------------

    def move_down(self):

        cell = self.maze[self.row][self.col]

        if not cell["bottom"] and self.row < self.rows - 1:
            self.row += 1

    # -----------------------------------------
    # Move Left
    # -----------------------------------------

    def move_left(self):

        cell = self.maze[self.row][self.col]

        if not cell["left"] and self.col > 0:
            self.col -= 1

    # -----------------------------------------
    # Move Right
    # -----------------------------------------

    def move_right(self):

        cell = self.maze[self.row][self.col]

        if not cell["right"] and self.col < self.cols - 1:
            self.col += 1

    # -----------------------------------------
    # Goal Check
    # -----------------------------------------

    def reached_goal(self):

        return (
            self.row == self.goal_row and
            self.col == self.goal_col
        )

    # -----------------------------------------
    # Reset Player
    # -----------------------------------------

    def reset(self):

        self.row = 0
        self.col = 0