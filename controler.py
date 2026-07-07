class GameController:

    def __init__(self, player):
        self.player = player

    def move(self, direction):

        direction = direction.upper()

        if direction == "UP":
            self.player.move_up()

        elif direction == "DOWN":
            self.player.move_down()

        elif direction == "LEFT":
            self.player.move_left()

        elif direction == "RIGHT":
            self.player.move_right()

        return self.player.get_position()