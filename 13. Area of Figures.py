import math

type_figure = input()
a = float(input())

if type_figure == 'square':
    square = a * a 
    print(round(square, 3))
elif type_figure == 'rectangle':
    b = float(input())
    rectangle = a * b
    print(round(rectangle, 3))    
elif type_figure == 'circle':
    circle = math.pi * (a * a)
    print(round(circle, 3))    
else:
    b = float(input())
    triangle = (a * b) / 2
    print(round(triangle, 3))    