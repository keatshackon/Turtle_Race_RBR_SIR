from turtle import Turtle,Screen
import random

my_screen = Screen()
# To set the Size of Screen First Argument for width And Second Argument For height
my_screen.setup(500,400)

is_game_on = False

# For Dailogue Box
user_bet = my_screen.textinput(title="Make a bet",prompt= "Which turtle you want to win ? Enter The Color")

colors = ["red","purple","black","green","cyan"]

y_corordinate = [0,-50,-100,50,100]
all_turtle = []

# Creating Five Instance of Turtle
for i in range(5):
    # Initialser in Constructor is For change The convert Arrow into Tuttle shape
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(-240,y_corordinate[i])
    all_turtle.append(new_turtle)

if user_bet:
    is_game_on = True

while is_game_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_game_on = False
            winning_color = turtle.pencolor()

            if winning_color == user_bet:
                print(f"You have won. The {winning_color} is the winner")
            else:
                print(f"You have lost. The {winning_color} is the Winner")
        
        rand_dis = random.randint(0,10)
        turtle.forward(rand_dis)





my_screen.exitonclick()