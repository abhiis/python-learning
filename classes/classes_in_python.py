class Point:
    def move(self):
        print("MOVE")

    def draw(self):
        print("DRAW")


point1 = Point()
point1.draw()
point1.move()
#can declare properties on these objects too as

point1.x = 10
point1.y = 20
print(point1.x, point1.y)
