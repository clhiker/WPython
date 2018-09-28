import random
import turtle

class Paint:
    def __init__(self):
        self.map = {""}
        self.paint_map = [([0] * 10) for i in range(10)]
        self.t = turtle.Turtle()

    def DrawFrame(self):
        self.t.goto(0+200, 0)
        self.t.goto(0 + 200, 0+200)
        self.t.goto(0, 0+200)
        self.t.goto(0, 0)

    def DrawLine(self):
        for i in range(1, 10):
            self.t.pencolor("white")
            self.t.goto(20 * i, 200)
            self.t.pencolor("black")
            self.t.goto(20 * i, 0)
        for i in range(1, 10):
            self.t.pencolor("white")
            self.t.goto(200, 20 * i)
            self.t.pencolor("black")
            self.t.goto(0, 20 * i)

    def SetRandom(self):
        for i in range(10):
            for j in range(10):
              self.paint_map[i][j] = 0
        for i in range(40):
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            self.paint_map[x][y] = 1

    def SetBarrir(self):
        self.SetRandom()
        for i in range(10):
            for j in range(10):
                if(self.paint_map[i][j] == 1):
                    self.PaintSquare(i, j)

    def PaintSquare(self, x, y):
        x *= 20
        y *= 20
        self.t.pencolor("white")
        self.t.goto(x, y)
        self.t.pencolor("black")
        self.t.fillcolor("red")
        self.t.begin_fill()
        self.t.goto(x + 20, y)
        self.t.goto(x + 20, y + 20)
        self.t.goto(x, y + 20)
        self.t.goto(x, y)
        self.t.end_fill()

    def paint(self):
        self.SetBarrir()
        self.DrawFrame()
        self.DrawLine()

def main():
    paint = Paint()
    paint.paint()
    turtle.done()
    paint.SetRandom()

main()