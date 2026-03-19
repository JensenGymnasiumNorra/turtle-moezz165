import turtle
import random

wn = turtle.Screen()
wn.title("Snake")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

score = 0

head = turtle.Turtle()
head.shape("turtle")
head.color("green")
head.penup()
head.goto(0,0)
head.direction = "stop"

food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()

pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(0,260)

game_text = turtle.Turtle()
game_text.hideturtle()
game_text.color("white")
game_text.penup()

segments = []

def new_food():
    x = random.randint(-280,280)
    y = random.randint(-280,280)
    food.goto(x,y)

new_food()

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

wn.listen()
wn.onkeypress(go_up,"Up")
wn.onkeypress(go_down,"Down")
wn.onkeypress(go_left,"Left")
wn.onkeypress(go_right,"Right")

def move():
    if head.direction == "up":
        head.sety(head.ycor()+20)
    if head.direction == "down":
        head.sety(head.ycor()-20)
    if head.direction == "left":
        head.setx(head.xcor()-20)
    if head.direction == "right":
        head.setx(head.xcor()+20)

def restart(x=None,y=None):
    global score
    score = 0
    pen.clear()
    game_text.clear()
    head.goto(0,0)
    head.direction = "stop"
    head.showturtle()
    for seg in segments:
        seg.goto(1000,1000)
    segments.clear()
    new_food()
    game_loop()

def game_over():
    game_text.goto(0,0)
    game_text.write(f"Game Over\nPoäng: {score}\nKlicka för att försöka igen",align="center",font=("Arial",16,"normal"))
    wn.onclick(restart)

def game_loop():
    global score
    wn.update()

    move()

    if abs(head.xcor())>290 or abs(head.ycor())>290:
        head.hideturtle()
        game_over()
        return

    for segment in segments:
        if head.distance(segment) < 20:
            head.hideturtle()
            game_over()
            return

    if head.distance(food)<20:
        new_food()
        score+=1
        segment=turtle.Turtle()
        segment.shape("square")
        segment.color("green")
        segment.penup()
        segments.append(segment)

    for i in range(len(segments)-1,0,-1):
        x=segments[i-1].xcor()
        y=segments[i-1].ycor()
        segments[i].goto(x,y)

    if len(segments)>0:
        segments[0].goto(head.xcor(),head.ycor())

    pen.clear()
    pen.write(f"Poäng: {score}",align="center",font=("Arial",16,"normal"))

    wn.ontimer(game_loop,100)

game_loop()
wn.mainloop()