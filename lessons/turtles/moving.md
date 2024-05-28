# Moving 


As we saw in the last example, Tina can move!  When she moves, she draws a line.  She can move `forward` and `backward` and turn `right` or `left` a certain number of degrees.

Run this example to see her move:
 
```python.run
import turtle
tina = turtle.Turtle()
tina.shape("turtle")

tina.forward(50)
tina.left(90)
# The forward command moves Tina in the direction it's facing. The units are pixels, so Tina moves 90 pixels forward.
# The "left" or "right" command rotates Tina a certain amount of degrees, specified by the next numbers. In this case, Tina rotates left 90 degrees.
tina.forward(50)
tina.left(90)

tina.forward(50)
tina.left(90)
```

She's almost made a square!  Can you help her complete it?  What other shapes can you help Tina draw?



---

Thanks to Trinket.io for providing this assignment, 
part of their [Hour of Python](https://hourofpython.com/a-visual-introduction-to-python/) 
course.