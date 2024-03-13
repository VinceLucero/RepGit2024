import turtle

# Create a turtle object
t = turtle.Turtle()

# Set the speed of the turtle
t.speed(2)

# Draw the outer circle
t.penup()
t.goto(0, -100)
t.pendown()
t.circle(100)

# Draw the inner circle
t.penup()
t.goto(0, -70)
t.pendown()
t.circle(70)

# Draw the pupil
t.penup()
t.goto(0, -40)
t.pendown()
t.begin_fill()
t.circle(40)
t.end_fill()

# Hide the turtle
t.hideturtle()

# Keep the window open
turtle.done()
