import turtle
tina = turtle.Turtle()
tina.shape("turtle")
tina.speed(0)

forward = 50
left = 90

def side(turtle, forward, left):
  turtle.forward(forward)
  turtle.left(left)


def make_shape(turtle, forward, left, sides):
  for i in range(sides):
    side(turtle, forward, left)

for sides in range(4, 6):
  make_shape(tina, forward, left, sides)