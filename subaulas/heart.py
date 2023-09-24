import turtle
tr = turtle.Turtle()
win = turtle.Screen()
win.setup(800, 800)
win.bgcolor("linen")
tr.speed(0)

colors = ["#FFB3D1", "#FF89BB", "#FF559D", "#D01769", "#D61951"]
down = -100
fward = 278
radius = -140

for c in colors:
    tr.penup()
    tr.goto(0, down)
    tr.color(c)
    tr.begin_fill()
    tr.left(140)
    tr.forward(fward)
    tr.circle(radius, 200)
    tr.setheading(60)
    tr.circle(radius, 200)
    tr.forward(fward)
    tr.end_fill()

    tr.setheading(0)
    down = down+20
    fward=fward-40
    radius = radius+20

tr.penup()
tr.goto(-20, -200)
tr.write("coração legal", align="center", font=("Forte", 45, "bold"))

tr.hideturtle()
turtle.done()