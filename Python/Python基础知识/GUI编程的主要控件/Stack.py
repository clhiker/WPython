class Stack:
    def __init__(self):
        self.items = []

    def empty(self):
        return len(self.items)==0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if(self.empty()):
            return False
        else:
            return self.items.pop()

    def top(self):
        if not self.empty():
            return self.items[len(self.items)-1]
        else:
            return False

    def size(self):
        return len(self.items)
