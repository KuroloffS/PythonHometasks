# Is point in circle 
import math
class Point():
  def __init__(self, x : float, y : float):
    self.x = x 
    self.y = y
class Point():
  def __init__(self, x : float, y : float):
    self.x = x 
    self.y = y    
  def distance_to(self, other_point : Point):
    return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
class Circle:
  def __init__(self, center : Point, radius):
    self.center = center
    self.radius = radius

  def contains(self, point):
    return self.center.distance_to(point) <= self.radius

point1 = Point(3, 4)
point2 = Point(6, 10)
circle = Circle(Point(5, 5), 5)

print("Point1:", (point1.x, point1.y))
print("Point1:", (point2.x, point2.y))
print("Distance between Point1 and Point2:", point1.distance_to(point2))
print("Is Point1 inside the circle?", circle.contains(point1))
print("Is Point2 inside the circle?", circle.contains(point2))

