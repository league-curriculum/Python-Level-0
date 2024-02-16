# Polygons

A few lessons ago you told Tony the Turtle how to make a square. Did you also
make a polygon, like a hexagon?


Remember how we told Tony to make a square with a loop. Here is the really important part: 

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


{{ trinket("polygon_1.py", width="100%", height="250", embed_type="python") | safe }}


