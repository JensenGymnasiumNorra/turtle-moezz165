"""
Alla kommandon för turtle finns i filen kommandon.md

Skriv kod där en turtle rör sig slumpmässigt. 
Om den kommer för långt bort ska den automatiskt åka tillbaks till mitten. 
Använd turtle.xcor() för att få sköldpaddans x-koordinat. 
Utöka koden med två turtles som rör sig slumpmässigt framåt. Låt dem tävla till en mållinje. Skriv ut vilken som vann! 
"""
import turtle
import random

screen = turtle.Screen()
screen.setup(800, 600)

t1 = turtle.Turtle()
t1.color("blue")
t1.penup()
t1.goto(-350, 100)
t1.pendown()

t2 = turtle.Turtle()
t2.color("red")
t2.penup()
t2.goto(-350, -100)
t2.pendown()

mål = 350

vinnare = None

while not vinnare:
    steg1 = random.randint(1, 10)
    steg2 = random.randint(1, 10)

    t1.forward(steg1)
    t2.forward(steg2)

    if abs(t1.xcor()) > 380:
        t1.penup()
        t1.goto(0, 100)
        t1.pendown()

    if abs(t2.xcor()) > 380:
        t2.penup()
        t2.goto(0, -100)
        t2.pendown()

    if t1.xcor() >= mål:
        vinnare = "Blå turtle vann!"
    if t2.xcor() >= mål:
        vinnare = "Röd turtle vann!"

print(vinnare)

turtle.done()
    