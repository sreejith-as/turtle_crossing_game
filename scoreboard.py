from turtle import Turtle

FONT = ("Courier", 24, "normal")  # Define the font style for the scoreboard text

class Scoreboard(Turtle):
    """
    A class to manage and display the player's score and level in the game.

    Inherits from the Turtle class and provides methods to update the scoreboard and display game over messages.

    Attributes:
        level (int): The current level of the game.
    """

    def __init__(self):
        """
        Initializes a new Scoreboard instance.

        Sets the initial level to 1, hides the turtle cursor, positions the scoreboard on the screen,
        and updates the scoreboard display.
        """
        super().__init__()  # Call the initializer of the parent Turtle class
        self.level = 1  # Initialize the level to 1
        self.hideturtle()  # Hide the turtle cursor
        self.penup()  # Prevent the turtle from drawing lines while moving
        self.goto(x=-280, y=260)  # Position the scoreboard at the top left of the screen
        self.update_scoreboard()  # Update the scoreboard display with the initial level

    def update_scoreboard(self):
        """
        Clears the current scoreboard display and writes the updated level.

        This method is called whenever the level changes to refresh the displayed score.
        """
        self.clear()  # Clear the previous scoreboard display
        self.write(f"Level: {self.level}", align="left", font=FONT)  # Write the current level on the screen

    def increase_level(self):
        """
        Increases the level by 1 and updates the scoreboard display.

        This method is typically called when the player successfully crosses the finish line.
        """
        self.level += 1  # Increment the level
        self.update_scoreboard()  # Update the scoreboard to reflect the new level

    def game_over(self):
        """
        Displays a 'Game Over' message at the center of the screen.

        This method is called when the game ends, either due to a collision or other game-over conditions.
        """
        self.goto(0, 0)  # Move the turtle to the center of the screen
        self.write("Game Over", align="center", font=FONT)  # Write the game over message