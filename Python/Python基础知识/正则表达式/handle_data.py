
import turtle
def SetRandom():
    paint_map = [([0] * 11) for i in range(11)]
    #paint_map = [[0 for i in range(11)] for j in range(11)]
    for i in range(11):
        for j in range(11):
            paint_map[i][j] = j*10
    print(paint_map)

def PaintSquare(x, y):
     t = turtle.Turtle()
     t.pencolor("white")
     t.goto(x, y)
     t.pencolor("black")
     t.fillcolor("red")
     t.begin_fill()
     t.goto(x + 20, y)
     t.goto(x + 20, y + 20)
     t.goto(x, y + 20)
     t.goto(x, y)
     t.end_fill()
     turtle.done()

SetRandom()
PaintSquare(0,0)