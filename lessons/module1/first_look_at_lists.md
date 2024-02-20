# First Look at Lists


Like we said before, a list is a lot like a list that you already know about, like a grocery list:

```
Things To Buy
  - apples
  - oranges
  - bread 
  - milk
```

But in Python we would write it like this: 

```python 
things_to_buy = [ 'apples','oranges','bread','milk']
```

The brackets, `[` and `]` are most often used to mean that something is a list. 

There are a lot of neat things we can do with a list.

First, you can get a specific item from a list, using the `[]` with a number inside. 

```python
things_to_buy[1]
> oranges
```

Getting values out of a list like this is called "indexing".


Like most programming languages, the first item in a list is 0, not 1, so if
you wanted to get `apples` from the list, you would write `things_to_get[0]`

Another important thing about lists is you can _iterate_ them, which means 'do
something repeatedly'. Here is how we would print out all of the items in the
list: 


```python.run
things_to_buy = [ 'apples','oranges','bread','milk']

for item in things_to_buy:
    print(item)
```

Loops and lists could be very useful for our turtle programs. For instance, we could make a square with 
a different color on each side: 

```python.run
import turtle
tina = turtle.Turtle()
tina.shape("turtle")

forward = 50
left = 90
colors = [ 'red', 'blue', 'black', 'orange']

for color in colors:
    tina.color(color)
    tina.forward(forward)
    tina.left(left)

```

Or, we could change the angle that tina turns: 

```python.run
import turtle
tina = turtle.Turtle()
tina.shape("turtle")

forward = 50

for left in [ 45, 60, 90, 45, -90, 60, 22 , -45, 90]:
    tina.forward(forward)
    tina.left(left)

```


Here is a way that we could change two variables at once, using array indexes:


```python.run
import turtle
tina = turtle.Turtle()
tina.shape("turtle")

forward = 50
lefts = [ 45, -60, 90, 45, -90, 60, 22 , -45 ]
colors = [ 'red', 'blue', 'black', 'orange', 'red', 'blue', 'black', 'orange']

for  i in range(8):
    left = lefts[i]
    color = colors[i]

    tina.color(color)
    tina.forward(forward)
    tina.left(left)

```


Now, write your own crazy program. You can copy and change the programs we've done previously.

```python.run:height=600
import turtle
tina = turtle.Turtle()
tina.shape("turtle")

```


