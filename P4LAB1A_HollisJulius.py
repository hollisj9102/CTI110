import turtle          
win = turtle.Screen()  
t = turtle.Turtle()

# add some display options
t.pensize(3)            # increase pensize (takes integer)
t.pencolor("blue")     # set pencolor (takes string)
t.shape("turtle")

#commands from here to the last line can be replaced
# triangle, sides are 360 / 3 = 120 degrees

t.forward(100)          
t.left(120)            
t.forward(100)
t.left(120)
t.forward(100)

# Move turtle to new position so shapes don't fully overlap
t.penup()
t.goto(100, 100)
t.pendown()

#commands from here to the last line can be replaced 

t.forward(50)          # Tell alex to move forward by 50 units
t.left(90)             # Tell alex to turn by 90 degrees
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)

# end commands
win.mainloop()             # Wait for user to close window
