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

The first line in the loop defines the loop and tells us how many times to do the body of the loop. The body of the loop, the ` print("Hello!")` part,  is indented. The ``range`` part will run the number of times inside the parenthesis, in this case 4. 

The `i` part is also special. This is called a variable, and we will learn more about them later. The most important thing now is that the indented part is repeated the number of times of the number in `range()`. 

Here is our way of solving the square exercise: 

{{ trinket("square-solved.py", width="100%", height="600", embed_type="python") | safe }}

Notice that there is a lot of repetition in this program. Can you edit this program to make it much better, by replacing the repetition with a loop?

Once you have used a loop to help Tony make a square, try making other shapes, like a triangle, a pentagon, or a hexagon, or maybe even a ... hendecagon. (if you can figure out what that is. )

