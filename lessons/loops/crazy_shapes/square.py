import turtle
tina = turtle.Turtle()
tina.shape("turtle")
tina.speed(0)

forward = 50
left = 90
sides = 4

def side(turtle, forward, left):
  turtle.forward(forward)
  turtle.left(left)

for i in range(sides):
  side(tina, forward, left)