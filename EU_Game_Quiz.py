import turtle
import pandas as pd
from tkinter import messagebox

screen = turtle.Screen()
screen.title('E.U Members Game')
image = 'europe.gif'
screen.addshape(image)
turtle.shape(image)

score = 0
EU_data = pd.read_csv('eu_members.csv')

Members = list(EU_data['member'])
x_values = list(EU_data['x'])
y_values = list(EU_data['y'])
Coordinates = list(zip(x_values, y_values))

Members_Dict = dict(zip(Members, Coordinates))

FONT = ('Arial', 10, 'bold')


def create_member(x, y, text):
    member = turtle.Turtle()
    member.hideturtle()
    member.penup()
    member.goto(x, y)
    member.color('yellow')
    member.write(text, align="center", font=FONT)


already_guessed = []

while score < len(Members):
    answer = screen.textinput(title=f"Guess the EU member  {len(already_guessed)}/27",
                              prompt="Please enter another member's name?").title()

    if answer in Members:
        if answer in already_guessed:
            messagebox.showinfo(title="Duplicate Guess",
                                message=f'{answer} is already on the map.')
        else:
            create_member(Members_Dict[answer][0],
                          Members_Dict[answer][1], answer)
            already_guessed.append(answer)
            score += 1
    else:
        messagebox.showinfo(title="Incorrect Guess",
                            message=f'{answer} is not in the EU.')


messagebox.showinfo(title="All EU Members", message="No more guesses Left.")

screen.exitonclick()
