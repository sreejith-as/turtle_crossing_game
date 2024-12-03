from turtle import Turtle

STARTING_POSITION = (0, -280)  # Starting position of the player
MOVE_DISTANCE = 10  # Distance the player moves with each step
FINISH_LINE_Y = 280  # Y-coordinate of the finish line

class Player(Turtle):
    """
    A class to represent the player in the turtle crossing game.

    Inherits from the Turtle class and provides methods to control the player's movement.

    Attributes:
        None (inherits from Turtle)
    """

    def __init__(self):
        """
        Initializes a new Player instance.

        Sets the shape of the player to a turtle, positions it at the starting position,
        and sets its heading to face upwards.
        """
        super().__init__()  # Call the initializer of the parent Turtle class
        self.shape("turtle")  # Set the shape of the player to a turtle
        self.penup()  # Prevent the player from drawing lines while moving
        self.go_to_start()  # Position the player at the starting position
        self.setheading(90)  # Set the heading to face upwards (90 degrees)

    def go_up(self):
        """
        Moves the player upwards by the defined MOVE_DISTANCE.
        """
        self.forward(MOVE_DISTANCE)  # Move the player forward (upwards)

    def go_down(self):
        """
        Moves the player downwards by the defined MOVE_DISTANCE.
        """
        self.backward(MOVE_DISTANCE)  # Move the player backward (downwards)

    def go_to_start(self):
        """
        Resets the player's position to the starting position.
        """
        self.goto(STARTING_POSITION)  # Move the player to the starting position

    def is_at_finish_line(self):
        """
        Checks if the player has reached the finish line.

        Returns:
            bool: True if the player is above the finish line, False otherwise.
        """
        if self.ycor() > FINISH_LINE_Y:  # Check if the player's Y-coordinate is above the finish line
            return True  # Player has reached the finish line
        else:
            return False  # Player has not yet reached the finish line