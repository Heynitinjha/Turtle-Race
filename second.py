from turtle import Turtle, Screen
import random

screen = Screen()
is_on = False
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make a bet", prompt="Which color turtle win the race ? ")
print(user_bet)
Colors = ["red", "blue", "green", "yellow", "orange", "grey"]
Y_Position = [-70, -40, -10, 20, 50, 80]
Turtle1 = []
for turtle_index in range(0, 6):
    timmy = Turtle(shape="turtle")
    timmy.color(Colors[turtle_index])
    timmy.penup()
    timmy.goto(x=-230, y=Y_Position[turtle_index])
    Turtle1.append(timmy)

if user_bet:
    is_on = True

while is_on:
    for turtle in Turtle1:
        if turtle.xcor() > 230:
            is_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f" you won, winning color is {winning_color}.")
            else:
                print(f"you loss, winning color is {winning_color}")
        random_position = random.randint(1, 10)
        turtle.forward(random_position)


screen.exitonclick()