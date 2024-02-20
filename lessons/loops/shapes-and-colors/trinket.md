Now it is your turn to try your own turtle program, by using hints from your previous programs. First, let's review your last turtle program: 

```python.run:height=400  
import turtle
tina = turtle.Turtle()
tina.shape("turtle")

tina.forward(50)
tina.left(90)
tina.forward(50)
tina.left(90)
tina.forward(50)
```

For the program you are going to write, you need to know one more thing: how to write a loop. A loop does something over and over. The loop in the program below is made by the line ``for i in range(4)``. This line will cause the indented code below if multiple times. First, guess how many times the turtle will print "Where Am I"
and then run the program to see if you are right.

```python.run:height=400 
import turtle
tina = turtle.Turtle()

tina.right(90)

for i in range(3):
    tina.forward(30)
    tina.write("Where Am I")
```

Now we can get to writing your own program. Use what you know about Tina the Turtle from previous programs, and what you've just learned about loops to write the program below. Read the comments for hints about what you should do. 

```python.run
import turtle


window = turtle.Screen()
window.bgcolor('white')

# This code makes a new Turtle. Pick a new 
# name for the turtle
my_turtle = turtle.Turtle()

# Make your turtle's shape 'turtle', .shape('turtle')

# Set your turtle's speed using .speed(2)

# Set your turtle's color using .color('green') 
# and .pencolor('blue')

# Move your turtle forward using .forward(100)
# TEST    Did your turtle move forward?

# Move your turtle left or right using .left(90) 
# or .right(90)

# Now put the forward and left/right code into a for 
# loop to repeat 4 times.
# TEST    Did your turtle draw a square?

# Move your turtle to a new place on the screen using .goto(x, y)
# x=0 and y=0 is the center of the screen

# Have your turtle draw a circle using .circle(radius, steps=30)
# TEST    Did your turtle draw a circle?

# Add color to your shape by adding .begin_fill() 
# before drawing the circle
# and .end_fill() below

# Draw 3 more shapes with different fill colors!

# ===================== DO NOT EDIT THE CODE BELOW ============================
turtle.done()
```


---

Thanks to Trinket.io for providing this assignment, 
part of their [Hour of Python](https://hourofpython.com/a-visual-introduction-to-python/) 
course.