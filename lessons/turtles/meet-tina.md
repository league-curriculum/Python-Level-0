# Meet Tina 

Tina is a Turtle that you control with code.  Press run to see what this program does, and see if you can figure out what line tells Tina to say,`"Why, hello there!"`

```python.run
import turtle
# the import command imports the turtle icon
tina = turtle.Turtle()
# tina is the variable. This command defines tina as the turtle
tina.shape('turtle')
# this makes tina's shape the turtle

tina.penup()
# This makes sure Tina doesn't write before she moves
tina.forward(20)
tina.write("Why, hello there!")
# You can replace the text in the quotation marks to change what Tina says. Give it a try!
tina.backward(20)
```

Don't worry if you don't understand all of the code.  You don't have to to get started, and more and more of it will become familiar to you as you keep going.

Use the arrow or click Next to go to the next example!

---

Thanks to Trinket.io for providing this assignment, 
part of their [Hour of Python](https://hourofpython.com/a-visual-introduction-to-python/) 
course.
