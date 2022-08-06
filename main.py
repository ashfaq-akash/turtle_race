import turtle
from turtle import Turtle,Screen
import random

is_race_on= False
new_turtle=Turtle()
screen=Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make the bet", prompt="Which turtle will win the race?Enter color: ")
colors=["red","orange","yellow","green","blue","purple"]
turtle_list=[]

for i in range(len(colors)):
    new_turtle=Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-100 )
    new_turtle.sety(30 * (i + 1))
    new_turtle.right(10)
    turtle_list.append(new_turtle)

if user_bet:
    is_race_on=True

while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor()>230:
            is_race_on = False
            win_turtle=turtle.pencolor()
            if win_turtle==user_bet:
                print(f"You have won. The {win_turtle} is winner!")

            else:
                print(f"You have lose. The {win_turtle} is winner!")

        distance=random.randint(0,10)
        turtle.forward(distance)


screen.exitonclick()