"""
Alla kommandon för turtle finns i filen kommandon.md

Den här uppgiften går ut på att designa en klocka med turtle:
Skriv ut siffror med turtle.write(“1”)
Använd for för att skriva ut alla siffror mellan 1 och 12 runt om i en cirkel
Designa klockan så att den blir snygg (den behöver inte ticka)
"""
import turtle
import math

t = turtle.Turtle()
t.speed(1)
cirkel_radie = 150
text_radie = 120

t.penup()
t.goto(0, -cirkel_radie)
t.pendown()
t.circle(cirkel_radie)
t.penup()

for i in range(1, 13):
    vinkel_grader = 90 - (i * 30)
    vinkel_radianer = math.radians(vinkel_grader)
    
    x = text_radie * math.cos(vinkel_radianer)
    y = text_radie * math.sin(vinkel_radianer)
    
    t.goto(x, y - 10)
    t.write(str(i), align="center", font=("Arial", 16, "normal"))

def rita_visare(siffra, tjocklek, langd):
    vinkel_grader = 90 - (siffra * 30)
    t.goto(0, 0)
    t.pendown()
    t.pensize(tjocklek)
    t.setheading(vinkel_grader)
    t.forward(langd)
    t.penup()

rita_visare(6, 5, 80)
rita_visare(7, 3, 90)

t.hideturtle()
turtle.done()