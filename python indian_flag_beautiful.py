import turtle
import time

# ---------- Screen Setup ----------
screen = turtle.Screen()
screen.setup(width=900, height=650)
screen.bgcolor("#EAF6FF")
screen.title("Indian National Flag - Turtle Graphics")
screen.tracer(0)  # speeds up drawing, we'll update manually

t = turtle.Turtle()
t.hideturtle()
t.speed(0.25)
time.sleep(1)

# ---------- Flag Dimensions ----------
flag_width = 600
flag_height = 400
stripe_height = flag_height / 3

start_x = -flag_width / 2 + 40   # shifted right to leave room for pole
start_y = flag_height / 2

# ---------- Helper: filled rectangle ----------
def draw_rectangle(x, y, width, height, color):
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)

    t.end_fill()

# ---------- Soft shadow behind flag (fixed: plain gray, no alpha) ----------
draw_rectangle(start_x + 8, start_y - 8, flag_width, flag_height, "#D3D3D3")

# ---------- Flag pole ----------
t.penup()
t.goto(start_x - 10, start_y + 60)
t.pendown()
t.pensize(10)
t.pencolor("#5C4033")
t.setheading(270)
t.forward(flag_height + 120)

# Pole finial (gold knob on top)
t.penup()
t.goto(start_x - 10, start_y + 70)
t.pendown()
t.fillcolor("#D4AF37")
t.begin_fill()
t.circle(12)
t.end_fill()

# ---------- Three Stripes ----------
draw_rectangle(start_x, start_y, flag_width, stripe_height, "#FF9933")   # Saffron
draw_rectangle(start_x, start_y - stripe_height, flag_width, stripe_height, "#FFFFFF")  # White
draw_rectangle(start_x, start_y - 2 * stripe_height, flag_width, stripe_height, "#138808")  # India Green

# ---------- Flag Border ----------
t.penup()
t.goto(start_x, start_y)
t.setheading(0)
t.pendown()
t.pensize(3)
t.pencolor("#333333")
for _ in range(2):
    t.forward(flag_width)
    t.right(90)
    t.forward(flag_height)
    t.right(90)

# ---------- Ashoka Chakra ----------
center_x = start_x + flag_width / 2
center_y = start_y - 1.5 * stripe_height
radius = stripe_height / 2.6

# Outer navy circle
t.penup()
t.goto(center_x, center_y - radius)
t.setheading(0)
t.pendown()
t.pencolor("#000080")
t.pensize(4)
t.circle(radius)

# 24 spokes
for i in range(24):
    angle = i * (360 / 24)
    t.penup()
    t.goto(center_x, center_y)
    t.setheading(angle)
    t.pendown()
    t.pensize(2)
    t.forward(radius)

# Small decorative dots at spoke tips
for i in range(24):
    angle = i * (360 / 24)
    t.penup()
    t.goto(center_x, center_y)
    t.setheading(angle)
    t.forward(radius)
    t.pendown()
    t.dot(6, "#000080")

# Center hub
t.penup()
t.goto(center_x, center_y - 6)
t.pendown()
t.fillcolor("#000080")
t.begin_fill()
t.circle(6)
t.end_fill()

# ---------- Caption ----------
t.penup()
t.goto(0, start_y - flag_height - 60)
t.pendown()
t.color("#333333")
t.write("Jai Hind", align="center", font=("Georgia", 22, "bold italic"))

screen.update()
turtle.done()