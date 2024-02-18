# Loops for Easy Squares

In this program, Tony the turtle is going to try to draw a square, but
he only gets it half done. Can you help him finish?

{{ trinket("square.py", width="100%", height="600", embed_type="python") | safe }}

Did you convince him to draw a whole square? If so, great! Let's look at how
a lot of programmers solve the problem, and see if we can do better. But first,
we need to know about loops. 

A loop is a bit of code that causes the computer to do something multiple times. 
Here is a loop for printing "Hello!" mutiple times. How many times do you think it will print?

{{ trinket("hello.py", width="100%", height="250", embed_type="python") | safe }}

Let's look at that in more detail:

```python
for i in range(4):
    print("Hello!")
```

The first line in the loop defines the loop and tells us how many times to do
the body of the loop. The body of the loop, the ` print("Hello!")` part,  is
indented. The ``range`` part will run the number of times inside the
parenthesis, in this case 4. 

The `i` part is also special; it is a variable. So, you could print it out too. 

```python
for i in range(4):
    print("Hello!", i)
```

Another interesting things with the loops is that `range` can have more than
one number in it. If we put in two numbers, the values of i will go from the first number
to _one minus_ the second number, so if you want to printout the numbers 4, 5, 6, 7, 
you would used `range(4,8)`:

Try that yourself. Write a program to print "Hello" and then all of the numbers from 10 to 20:

{{ trinket("hello_10_20.py", width="100%", height="600", embed_type="python") | safe }}


But there are more interesting things about `range()`: It can take a _third_ number, and
all three of the numbers can be negative or positive. Let's explore `range()` to 
figure out what the third number does. 


{{ trinket("hello_explore_range.py", width="100%", height="600", embed_type="python") | safe }}


## Make a Better Square. 

Here is our way of solving the square exercise: 

{{ trinket("square-solved.py", width="100%", height="600", embed_type="python") | safe }}

Notice that there is a lot of repetition in this program. Can you edit this
program to make it much better, by replacing the repetition with a loop?

Once you have used a loop to help Tony make a square, try making other shapes,
like a triangle, a pentagon, or a hexagon, or maybe even a ... hendecagon.
(if you can figure out what that is. )

