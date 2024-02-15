import random
import turtle


# Returns a random color!
def getRandomColor():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


# ====================== DO NOT EDIT THE CODE ABOVE ===========================

window = turtle.Screen()  # ;
window.bgcolor("white")  # ;

# Make a new turtle
myTurtle = turtle.Turtle()  # ;

# This code sets our shape to a turtle
myTurtle.shape("turtle")  # ;

# Set your turtle's speed
myTurtle.speed(0)  # ;

# Set your turtle's color
myTurtle.color("green")  # ;

# Use a loop to repeat the code below 50 times
for i in range(50):  # ;

    # Set the turtle color to a random color
    myTurtle.pencolor(getRandomColor())  # ;

    # Move the turtle (5*i) pixels. 'i' is the loop variable
    myTurtle.forward(5 * i)  # ;

    # Turn the turtle (360/7) degrees to the right
    myTurtle.right(360 / 7)  # ;

    # Change the turtle width to 'i' (the loop variable)
    myTurtle.width(i)  # ;

    # Check the pattern against the picture in the recipe. If it matches, you are done!

# ===================== DO NOT EDIT THE CODE BELOW ============================
turtle.done()
