class Node:
    def __init__(self, value, tail):
        self.Value = value
        self.Tail = tail
        self.IsEmpty = False

class Empty:
    def __init__(self):
        self.IsEmpty = True

Empty = Empty()

class Position:
    def __init__(self, posx, posy):
        self.PositionX = posx
        self.PositionY = posy
