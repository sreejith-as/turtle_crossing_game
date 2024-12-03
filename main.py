import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Set up the screen for the game
screen = Screen()
screen.setup(width=600, height=600)  # Set the dimensions of the screen
screen.tracer(0)  # Disable automatic screen updates for smoother animation

# Initialize game components
player = Player()  # Create a player instance
car_manager = CarManager()  # Create a car manager instance to handle cars
scoreboard = Scoreboard()  # Create a scoreboard instance to display the score and level

# Listen for keyboard input to control the player
screen.listen()
screen.onkeypress(player.go_up, "Up")  # Move player up on 'Up' key press
screen.onkeypress(player.go_down, "Down")  # Move player down on 'Down' key press

# Main game loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)  # Pause for a short duration to control game speed
    screen.update()  # Update the screen

    car_manager.create_cars()  # Create new cars
    car_manager.move_cars()  # Move existing cars

    # Check if player has moved out of bounds (below the starting line)
    if player.ycor() < -280:
        player.go_to_start()  # Reset player position to start

    # Detect collision between player and cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:  # Check if the distance between car and player is less than 20
            game_is_on = False  # End the game if a collision is detected
            scoreboard.game_over()  # Display game over message

    # Check if player has reached the finish line
    if player.is_at_finish_line():
        player.go_to_start()  # Reset player position to start
        car_manager.level_up()  # Increase the level of the game
        scoreboard.increase_level()  # Update the scoreboard with the new level

# Exit the game when the screen is clicked
screen.exitonclick()