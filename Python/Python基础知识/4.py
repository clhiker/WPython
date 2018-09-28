import turtle
def tangle(t,x,y,w,h,colorp,colorF):
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

def dot(t,x,y,r,colorp):
  t.up()
  t.goto(x,y)
  t.pencolor(colorp)
  t.dot(r)
  
def main():
  t = turtle.Turtle()
  t.hideturtle()
  tangle(t,0,0,100,150,"red","yellow")
  dot(t,12,23,70,"red")
 

main()
