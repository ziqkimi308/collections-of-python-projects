# Import
from turtle import Screen
import time
from scoreboard import Scoreboard
from snake import Snake
from food import Food

# Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Create snake body, food, and scoreboard
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Capture key command to move snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Looping for snake to always moving
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1) # The animation updated 0.1 sec after
    # Call move
    snake.move()

    # Detect collision with food, extend segment, update scoreboard, and generate random food location
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_scoreboard()

    # Detect collision with wall
    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280:
        # game_is_on = False
        # scoreboard.game_over()
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    for i in snake.segments[1:]: # Slicing
        if snake.segments[0].distance(i) < 10:
            # game_is_on = False
            # scoreboard.game_over()
            scoreboard.reset()
            snake.reset()

# Last
screen.exitonclick()

