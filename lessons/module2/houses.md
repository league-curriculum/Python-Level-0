# Drawing Houses

Practice writing and calling functions that take parameters by making 
the turtle draw a row of houses.

 
1) Move the turtle to the left side of the window near the bottom.
2) Draw ONE flat-topped house with height=100 and green grass after it.
3) Put the code that drew the house into a function called draw_house
   HINT: Only the code that draws one house should go in this function.
4) Using the function you just created, draw 10 houses.
   HINT: Use a for loop.
5) Run the code to make sure it works before proceeding.
6) Now change the draw_house function to take height as a parameter.
7) Use random numbers to draw 9 houses of different heights.
8) Run the code to make sure it works before proceeding.
9) Make the draw_house function's height input a string and set the
   height of the house based on the following:
      “small”            =  60
      “medium”           =  120
      “large”            =  250
10) Make two new functions that draw different shaped roofs
   (JUST the roof part): draw_pointy_roof, draw_flat_roof
11) By calling the correct "roof" function, make large houses have
   flat roofs and all the others have pointy roofs.


Here is how to get random numbers:

```python.run
from random import randint

#get a number between 10 and 100
lowest = 10
highest = 100
num = randint(lowest, highest)
print(num)
```


## Draw Houses



```python.run:height=800




```


