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

{{ trinket("shapes-and-colors_1.py", width="100%", height="800", embed_type="python") | safe }}

Don't worry if you don't understand all of the code.  You don't have to to get started, and more and more of it will become familiar to you as you keep going.

Use the arrow or click Next to go to the next example!

---

Thanks to Trinket.io for providing this assignment, 
part of their [Hour of Python](https://hourofpython.com/a-visual-introduction-to-python/) 
course.