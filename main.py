from turtle import Turtle,Screen
from os import system
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
screen=Screen()
screen.setup(600,600)
screen.bgcolor('black')
screen.title('Snake Game 🐍')
screen.tracer(0)

snake=Snake()
scoreboard=Scoreboard()
scoreboard.update_score()
food=Food()


screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')

is_game_on=True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move() 

    # detect the collison with food
    if(snake.timy[0].distance(food)<15):
        food.refresh()
        scoreboard.increase_score()
        snake.extended_timy()

    # detect the collison with wall
    if(snake.timy[0].xcor()>280 or snake.timy[0].xcor()<-295 or snake.timy[0].ycor()>295 or snake.timy[0].ycor()<-295):
        is_game_on=False      
        scoreboard.game_over()  

    # detect the collison with tail  
        
   


    
screen.exitonclick()
system('cls')