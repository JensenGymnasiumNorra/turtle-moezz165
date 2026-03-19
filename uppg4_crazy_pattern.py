"""
Alla kommandon för turtle finns i filen kommandon.md

Använd for-loop för att göra mönster. Go crazy.

Exempel på slumpad färg och storlek:
- random.choice(lista) - väljer ett slumpmässigt element från en lista
- random.randint(min, max) - slumpar ett heltal mellan min och max
"""
import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")

padda = turtle.Turtle()
padda.speed(0) 
padda.width(2)

farger = ["red", "blue", "green", "yellow", "purple", "orange", "cyan", "magenta", "white"]

for i in range(60):
    padda.pencolor(random.choice(farger))
    padda.pensize(random.randint(1, 4))
    for _ in range(6):
        padda.forward(100)
        padda.right(60)
    padda.right(6)
    padda.forward(10)

turtle.done()