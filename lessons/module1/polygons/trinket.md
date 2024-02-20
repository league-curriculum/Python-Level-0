# Polygons

A few lessons ago you told Tony the Turtle how to make a square. Did you also
make a polygon, like a hexagon?


Remember how we told Tony to make a square with a loop. Here is the really
important part of that program: 

```python
for i in range(4):
    tony.forward(50)
    tony.left(90)

```

Notice that Tony turned *90* degrees each time, and he turned *4* times. How
many degrees did he turn in total? Well, 90 * 4 == 360, right? And what is
turning 360 degrees? Its turning back to where you started!

For every polygon, if Tony is going to get back to where he started,  needs to
turn 360 degrees, no matter how many sides it has. So, lets combine what we've learned
about loops and variables to make Tony make other shapes. 


{{ trinket("polygon_1.py", width="100%", height="500", embed_type="python") | safe }}


Now see if you can use 2 loops to make Tony make multiple shapes. Here is a
hint: In the loop statement with the range, like `for i in rage(4)`, the `i`
is a variable that you can use like other variables in your program. Also,
range can take two numbers; the first is the starting number, and the second
is one more than the ending number.

{{ trinket("range.py", width="100%", height="250", embed_type="python") | safe }}


Now, can you use this new information to add a second loop to your program
that makes Tony draw multiple shapes?
