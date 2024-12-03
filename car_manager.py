import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    """
    A class to manage the cars in the game.

    Attributes:
        all_cars (list): A list that holds all the car objects.
        car_speed (int): The speed at which the cars move across the screen.
    """

    def __init__(self):
        """Initializes a new CarManager instance with an empty list of cars and a starting speed."""
        self.all_cars = []  # List to store all car instances
        self.car_speed = STARTING_MOVE_DISTANCE  # Set initial speed of cars

    def create_cars(self):
        """
        Randomly creates a new car and adds it to the list of cars.

        A new car is created with a 1 in 6 chance. The car is represented as a Turtle object,
        has a random color, and is positioned off-screen to the right at a random vertical position.
        """
        random_chance = random.randint(1, 6)  # Randomly decide whether to create a car
        if random_chance == 6:  # 1 in 6 chance to create a car
            new_car = Turtle("square")  # Create a new car as a square shape
            new_car.shapesize(stretch_wid=1, stretch_len=2)  # Set the size of the car
            new_car.penup()  # Prevent the car from drawing lines
            new_car.color(random.choice(COLORS))  # Assign a random color to the car
            random_y = random.randint(-230, 250)  # Generate a random vertical position
            new_car.goto(x=300, y=random_y)  # Position the car off-screen to the right
            self.all_cars.append(new_car)  # Add the new car to the list of cars

    def move_cars(self):
        """
        Moves all cars in the list backward by the current car speed.
        
        This simulates the movement of cars towards the left side of the screen.
        """
        for car in self.all_cars:
            car.backward(self.car_speed)  # Move each car backward by the current speed

    def level_up(self):
        """
        Increases the speed of the cars by a predefined increment.

        This method is called to increase the difficulty of the game as the player progresses.
        """
        self.car_speed += MOVE_INCREMENT  # Increase the speed of the cars