import turtle
def drawFilledRectangle(t,x,y,w,h,colorp="black",colorF="white"):
      t.pencolor(colorp)
      t.fillcolor(colorF)
      t.up()
      t.goto(x,y)
      t.down()
      t.begin_fill()
      t.goto(x+w,y)
      t.goto(x+w,y+h)
      t.goto(x,y+h)
      t.goto(x,y)
      t.end_fill()

def main():
  t = turtle.Turtle()
  t.hideturtle()
  drawFilledRectangle(t,0,0,100,150,"red","yellow")
  
 

main()
