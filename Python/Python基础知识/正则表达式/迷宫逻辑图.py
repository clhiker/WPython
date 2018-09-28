
import random

class LogicMaze:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.value = 0
        self.logic_map = [([0] * 12) for i in range(12)]

    def LogicPaint(self):
        for i in range(12):
            self.logic_map[i][0] = 1
            self.logic_map[0][i] = 1
            self.logic_map[11][i] = 1
            self.logic_map[i][11] = 1
        print(self.logic_map)

    def GetMaze(self):
        self.logic_map[10][1] = 0
        self.logic_map[1][10] = 0
        #绘出一条从首到尾的不交叉线
        ran = [1,2,3,4,5]
        setPoint = {}
        for i in range(20):





def main():
    lmaze = LogicMaze()
    lmaze.LogicPaint()

main()