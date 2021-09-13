class Point:
    def __init__(self, x, y):  #self === this
        self.x = x
        self.y = y

    def move(self):
        print(f"MOVE to ({self.x},{self.y})")

    def draw(self):
        print("DRAW")


point1 = Point(10, 20)
point1.move()
