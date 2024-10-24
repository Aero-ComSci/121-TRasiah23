import turtle as trtl
import random as rd

font_setup = ("Arial", 20, "normal")
timer = 30
counter_interval = 1000
timer_up = False
score = 0

tn = trtl.Turtle()
tn.hideturtle()
tn.penup()
tn.goto(0, 100)

score_display = trtl.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.goto(200, 100)

counter = trtl.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(-200, 100)

turtle = trtl.Turtle()
original_color = "pink"
turtle.shape("circle")
turtle.color(original_color)
turtle.shapesize(2)
turtle.penup()

colors = ["red", "blue", "green", "yellow", "purple", "orange"]
move_distance = 100

def change_color():
    global original_color
    original_color = rd.choice(colors)
    turtle.color(original_color)

def move_turtle():
    x = rd.randint(-200, 200)
    y = rd.randint(-200, 200)
    turtle.goto(x, y)
    change_color()
    turtle.stamp() 

def countdown():
    global timer, timer_up
    counter.clear()
    score_display.clear()
    
    if timer <= 0:
        counter.write("Time's Up", font=font_setup)
        timer_up = True
    else:
        counter.write("Timer: " + str(timer), font=font_setup)
        score_display.write("Score: " + str(score), font=font_setup)
        timer -= 1
        move_turtle()
        counter.getscreen().ontimer(countdown, counter_interval)

def spot(x, y):
    global score
    if not timer_up and turtle.distance(x, y) < 20:
        score += 1
        print("Score:", score)

wn = trtl.Screen()
wn.bgcolor("Cyan")
wn.ontimer(countdown, counter_interval)
wn.onclick(spot)
wn.mainloop()
