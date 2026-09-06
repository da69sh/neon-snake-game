from turtle import Turtle, Screen
import time
from food import Food
from score import Score
from snake import Snake
BG_COLOR = "#0A0E27"  # Dark navy
BORDER_COLOR = "#00FF41"
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


screen = Screen()
screen.setup(width=600, height=600)

screen.bgcolor(BG_COLOR)
screen.title("🐍 Snake Game 🐍")   
screen.tracer(0)

# Draw border
border = Turtle()
border.speed(0)
border.penup()
border.hideturtle()
border.color(BORDER_COLOR)
border.pensize(3)
border.goto(-300, 300)
border.pendown()
for _ in range(4):
    border.forward(600)
    border.right(90)

segments = []

Scoreboard = Score()
snake = Snake()
food = Food()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


while True:
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()
        snake.wrap_edges()
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            Scoreboard.increase()
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                Scoreboard.game_over()
                screen.update()
                break

    time.sleep(2)
    snake.reset()
    food.refresh()
    Scoreboard.reset_round()


  



screen.exitonclick()