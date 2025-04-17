from turtle import Turtle

     
timy_position=[-20,0,20]
UP=90
RIGHT=0
DOWN=270
LEFT=180
class Snake:
    def __init__(self):
        self.timy=[]
        self.creat_snake()
  


    def creat_snake(self):
        for pos in timy_position:
            self.add_timy(pos,0)

    def add_timy(self,x,y):
        timy=Turtle(shape='square')
        timy.color('white')
        timy.penup()
        timy.goto(x,y)
        self.timy.append(timy)   

    def extended_timy(self):
        self.add_timy(self.timy[-1].xcor(),self.timy[-1].ycor())

       
    def move(self):
        for timy in range(len(self.timy)-1,0,-1):
            new_x=self.timy[timy-1].xcor()
            new_y=self.timy[timy-1].ycor()
            self.timy[timy].goto(new_x,new_y)
        self.timy[0].forward(20) 


    def up(self):
        if self.timy[0].heading()!=DOWN:
            self.timy[0].setheading(UP)
    def right(self):
        if self.timy[0].heading()!=LEFT:
            self.timy[0].setheading(RIGHT)
    def left(self):
        if self.timy[0].heading()!=RIGHT:
            self.timy[0].setheading(LEFT)
    def down(self):
        if self.timy[0].heading()!=UP:
            self.timy[0].setheading(DOWN) 

    


    


