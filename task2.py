import math

def triangle_area(base, height):
    return 0.5 * base * height

def rectangle_area(width, height):
    return width * height
    
def circle_area(radius):
    return math.pi * radius ** 2
print("Triangle area:", triangle_area(10, 5))
print("Rectangle area:", rectangle_area(4, 6))
print("Circle area:", circle_area(3))