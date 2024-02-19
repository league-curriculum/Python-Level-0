Tina's world is a grid of squares like the one we sometimes use to graph in Algebra and Geometry.  

<iframe src="//player.vimeo.com/video/107876386?title=0&amp;byline=0&amp;portrait=0" width="710" height="249" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>

We can tell Tina to go directly to a specific point on the graph.  This makes it easy to teach her to draw something!

{{ trinket("tinas-grid_1.py", width="100%", height="800", embed_type="python") | safe }}

The grid goes from -200 to 200 in both directions.  You can send Tina to points outside her grid, but then you won't see what she's doing.

{{ trinket("tinas-grid_2.py", width="100%", height="800", embed_type="python") | safe }}

Play around drawing with Tina.  Send her to other points on the grid with a new line like this:

```python
tina.goto(37,-50)
```
You can pick whatever numbers you want, but they must be between `-200` and `200` for you to see them.

---

Thanks to Trinket.io for providing this assignment, 
part of their [Hour of Python](https://hourofpython.com/a-visual-introduction-to-python/) 
course.