"""
Alla kommandon för turtle finns i filen kommandon.md

Använd for-loop för att göra mönster. Go crazy.

Exempel på slumpad färg och storlek:
- random.choice(lista) - väljer ett slumpmässigt element från en lista
- random.randint(min, max) - slumpar ett heltal mellan min och max
"""
import turtle
import random

# Skapa en turtle
padda = turtle.Turtle()

# Exempel: Lista med färger att välja från
farger = ["red", "blue", "green", "yellow", "purple", "orange"]
padda.pencolor(random.choice(farger))  # Slumpar en färg från listan
padda.pensize(random.randint(1, 10))   # Slumpar pennans storlek mellan 1 och 10


turtle.done()