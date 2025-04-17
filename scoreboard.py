from turtle import Turtle
font=('courier',13,'normal')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0,280)
        self.score=0

    def update_score(self):
        self.write(f"Your Score : {self.score}",False,"center",font)

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",False,"center",font)


    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_score()    
        