"""
Alla kommandon för turtle finns i filen kommandon.md
Skapa en ny turtle
Rita en kvadrat med .forward och .right
Lyft upp din turtles penna genom att använda .penup()
Flytta nu till en annan punkt (x,y) genom att använda .goto(x,y)
Rita en till kvadrat med hjälp av .goto(x,y) som inte överlappar med den första kvadraten.
"""
import turtle

t = turtle.Turtle()

for _ in range(4):
    t.forward(100)
    t.right(90)

t.penup()
t.goto(150, 150)
t.pendown()

punkter = [(250, 150), (250, 50), (150, 50), (150, 150)]

for x, y in punkter:
    t.goto(x, y)

turtle.done()