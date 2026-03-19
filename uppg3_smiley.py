"""
Alla kommandon för turtle finns i filen kommandon.md
Nu ska du göra en smiley. Börja med att göra tre variabler: storlek på huvudet, storlek på ögonen och storlek på munnen.
Rita en smiley med turtle och använd variablerna så att smileyn lätt kan ändras.
"""

import turtle

storlek_huvud = 100
storlek_ogon = 10
storlek_mun = 50

t = turtle.Turtle()
t.speed(3)

t.circle(storlek_huvud)

t.penup()
t.goto(-40, 100)
t.pendown()
t.begin_fill()
t.circle(storlek_ogon)
t.end_fill()

t.penup()
t.goto(40, 100)
t.pendown()
t.begin_fill()
t.circle(storlek_ogon)
t.end_fill()

t.penup()
t.goto(0, 60)
t.pendown()
t.setheading(-60)
t.circle(storlek_mun, 120)

turtle.done()