import time
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scorecard import Scoreboard


def setup_screen():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Akku's Snake Game")
    screen.tracer(0)
    return screen


def setup_snake_controls(snake, screen):
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")


def main():
    screen = setup_screen()
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()
    setup_snake_controls(snake, screen)

    game_on = True
    while game_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Check collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            scoreboard.score_plus()

        # Check boundary collision
        if (snake.head.xcor() > 280 or snake.head.xcor() < -280 or
                snake.head.ycor() > 280 or snake.head.ycor() < -280):
            game_on = False
            scoreboard.game_over()

        # Check collision with own body
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 3:
                game_on = False
                scoreboard.game_over()

    screen.exitonclick()


if __name__ == "__main__":
    main()
