import turtle
from math import sin
from tkinter import *

root = Tk()
root.resizable(width=False, height=False)
root.title("Lissajou")


def get_counters():
    big_a = 200
    big_b = 200
    value_a = int(myA.get())
    value_b = int(myB.get())
    delta = 3.14 / 2
    t = 0
    window = turtle.Screen()
    window.clear()
    window.bgcolor("#000000")
    turtul = turtle.Turtle()
    turtul.hideturtle()
    turtul.speed(0)
    turtul.pensize(3)
    turtul.color("#FF30FF")

    turtul.penup()

    for i in range(0, 1000):
        t += 0.01
        x = big_a * sin(value_a * t + delta)
        y = big_b * sin(value_b * t)

        turtul.goto(x, y)
        turtul.pendown()
        turtul.getscreen().update()


myHeader = Label(root, text="Krzywe Lissajou")
myHeader.grid(columnspan=2, row=0)
myStringA = Label(root, text="wprowadz a:")
myStringA.grid(column=0, row=1)
myStringB = Label(root, text="wprowadz b:")
myStringB.grid(column=1, row=1)
myA = Entry(root)
myA.grid(column=0, row=2)
myB = Entry(root)
myB.grid(column=1, row=2)
sendButton = Button(root, text="Rysuj", command=get_counters)
sendButton.grid(columnspan=2, row=3)
root.mainloop()
