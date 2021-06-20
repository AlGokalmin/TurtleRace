from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput("Making your bet", "Which turtle will win the race? Please enter a color.")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []


for turtle_index in range(len(colors)):
    new_frog = Turtle(shape="turtle")
    new_frog.penup()
    new_frog.color(colors[turtle_index])
    new_frog.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_frog)

if bet in colors:
    is_race_on = True
else:
    print("PLease select a proper color")

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == bet:
                print(f"You won! The {winning_color} is the winner!")
            else:
                print(f"You lost! The {winning_color} is the winner!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
