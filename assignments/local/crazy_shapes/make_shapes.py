import turtle
tina = turtle.Turtle()
tina.shape("turtle")
tina.speed(0)


def side(turtle, forward, left):
  turtle.forward(forward)
  turtle.left(left)

def make_shape(forward, left, sides):
  for i in range(sides):
    side(tina, forward, left)


make_shape(50, 90, 4)