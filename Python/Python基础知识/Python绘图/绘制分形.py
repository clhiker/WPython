import turtle

def draw(t,x1,y1,x2,y2):
  t.up()
  t.goto(x1,y1)
  t.down()
  t.goto(x2,y2)
  
def fract(t,x1,y1,x2,y2,level):
  newX = 0
  newY = 0
  if level == 0:
    draw(t,x1,y1,x2,y2)
  else:
    newX = (x1+x2)/2+(y2-y1)/2
    newY = (y1+y2)/2-(x2-x1)/2
    fract(t,x1,y1,newX,newY,level-1)
    fract(t,newX,newY,x2,y2,level-1)

def main():
  t=turtle.Turtle()
  t.hideturtle()
  t.speed(0)
  level = 12
  fract(t,-80,60,80,60,level)
  turtle.Turtle().screen.delay(0)
main()
