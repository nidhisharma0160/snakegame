import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(height = 600, width = 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    score.update_score()

    #detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()
    # detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score.reset_game()
        snake.reset_snake()

    # detect collision with its tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset_game()
            snake.reset_snake()




















screen.exitonclick()