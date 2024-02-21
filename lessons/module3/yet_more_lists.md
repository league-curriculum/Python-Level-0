# Unpacking Tuples

Python has a neat feature called "Unpacking". You can assign a list to multiple
variables at once!

So, you already know how to do this:

```python 
x = 10
```

But, you can also do this:

```python 

# Unpacking
x, y = 10, 20

# Same thing, but boring
x = 10
y = 20
```

Unpacking involves something called a _tuple_. A tuple is like a list, but
unlike a list, you can't change it once it is created. Tuples are created by
putting commas between things, and you can put parentheses around it to make
it more clear. So these are all tuples:

```python.run

t1 = 1,2,3
print(t1)

t2 = (1,2,3)
print(t2)

# A tuple with one item!
t3 = 6, 
print(t3)
```

You can assign one tuple to another, but (mostly) they have to be the same
size. ( they can be different sizes but we'll save that for later. ) 


```python.run
t1 = 1,2,3
print(t1)
x,y,z = t1
print(x)
print(y)
print(z)

```

But the code below would be an error, because on the left side, the tuple has three
elements, but there are only two on the left. 


```python.run
t1 = 1,2,3
print(t1)

x,y = t1
print(x)
print(y)

```

Now that you know about tuples, you will see them in a lot of places in Python programs. 

## Zip and Enumerate

The really important part about tuples is when they are used in two important
functions, `enumerate()` and `zip()`


Enumerate means "to count out, one by one", and the `enumerate()` finction will count things for us. Here is how we use it:


```python.run

l = ['zero', 'one', 'two', 'three',' four']


for e in enumerate(l):
    print(e)
```

Hmmm .. it looks like it printed out tuples! In each tuple, the first element
is the number, and the second is the item. But, we know that we can unpack
tuples, so we could also write: 


```python.run

l = ['zero', 'one', 'two', 'three',' four']

# change 'e' to numnber, item
for number, item in enumerate(l): 
    print(str(number) + " " + str(item))
```

Enumerate is a very powerful way to count the things that we are iterating over. 


The `zip()` function is another very important function. Zip takes one or more
iterables, like strings, lists and tuples, and returns a tupe with the first one from each, then the second, then the third. 

```python.run

l = ['one', 'two', 'three', 'four', 'five']
t = ('uno', 'dos', 'tres', 'cuatro', 'cinco')
s = "12345"

for e in zip(l, t, s):
    print(e)

# or, Unpack!
print("")
for a, b, c in zip(l, t, s):
    print(str(a) + " " + str(b) + " " +str(c))

```

As you can see, the first tuple is the first item from each of the iterables.
The second tuple is the second item from all of the tuples, etc. 


## A Zippy Program


Write a program that has three lists or tuples that have commands for your turtle.
* One list has 10 distances to move ( `forward` from our previous programs). 
* One list has the direction to turn ( called `left` in past programs )
* One list has colors for the turle's pen

Zip all of the lists together, then unpack them in a loop, and call a function
with the values that makes your turtle change color, turn, and move. 

```python.run:height='600'


```

::: details Click me for a hint
```python 

turtle = ...

moves = [ ... ]
turns = [ ... ]
colors = [ ... ]


def move_turtle(..., ..., ...):
    turtle.color(...)
    turtle.forward(...)
    turtle.turn(...)


for move, turn color in zip(...):
    ...


```
:::

