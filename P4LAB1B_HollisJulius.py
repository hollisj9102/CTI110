import turtle          
win = turtle.Screen()  
t = turtle.Turtle()

# add some display options
t.pensize(3)            # increase pensize (takes integer)
t.pencolor("purple")     # set pencolor (takes string)
t.shape("turtle")

# --- Draw first initial: J ---
t.penup()
t.goto(-60, 50)
t.setheading(0)
t.pendown()

t.forward(40)       # Top bar of J
t.backward(20)
t.right(90)
t.forward(90)       # Downward stroke
t.setheading(250)   # Face left for bottom curve
t.circle(-20, 150)   # Curve left

# --- Move to position for second initial ---
t.penup()
t.goto(50, 50)
t.setheading(270)
t.pendown()

# --- Draw second initial: H ---
t.forward(100)
t.penup()
t.goto(50 + 40, 50)
t.setheading(270)
t.pendown()
t.forward(100)
t.penup()
t.goto(50, 0)
t.setheading(0)
t.pendown()
t.forward(40)

# Finish
t.hideturtle()
wn.mainloop()

