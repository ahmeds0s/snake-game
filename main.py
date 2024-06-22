from snake import Snake
from turtle import Turtle, Screen
import time
from scoreboard import ScoreBoard
from food import Food

# creating object screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)
# creating object snake
snake = Snake()
# creating object food
food = Food()
# creating object scoreboard
scoreboard = ScoreBoard(0)
# listing to the changes in screen in order to use key clicks as events
screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")



# routine of the game
def game_routine(snake, screen:Screen, scoreboard, food):
    game_is_on = True
    while game_is_on:
        # updating the screen each time we run in the loop
        screen.update()
        # get a time delay between each update and the other
        time.sleep(0.1)
        # let the snake move
        snake.move()
        # checking if the snake eat some food
        if snake.head.distance(food) < 20:
            food.refresh()
            snake.grow()
            scoreboard.increase_score()
        # checking if the snake hit the wall
        if abs(snake.head.xcor()) > 280 or abs(snake.head.ycor()) > 280:
            scoreboard.gameover()
            snake.Reset()
            snake = Snake()
            game_is_on = False

        # checking if the snake ate itself
        for segment in snake.segment[1:]:
            if snake.head.distance(segment) < 10:
                scoreboard.gameover()
                snake.Reset()
                snake = Snake()
                game_is_on = False
    screen.clear()
    game_over(scoreboard.get_highest_score())
def game_over(highest_score):
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake game")
    screen.tracer(0)
    # creating object snake
    snake = Snake()
    # creating object food
    food = Food()
    # creating object scoreboard
    scoreboard = ScoreBoard(highest_score)
    # listing to the changes in screen in order to use key clicks as events
    screen.listen()
    screen.onkey(snake.up, "w")
    screen.onkey(snake.down, "s")
    screen.onkey(snake.left, "a")
    screen.onkey(snake.right, "d")
    game_routine(snake, screen, scoreboard, food)
                


game_routine(snake, screen, scoreboard, food)
screen.exitonclick()

