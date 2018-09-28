import turtle
def dot(t,x,y,r,colorp):
  t.up()
  t.goto(x,y)
  t.pencolor(colorp)
  t.dot(r)

def main():
  t = turtle.Turtle()
  dot(t,12,23,300,"red")

main()
