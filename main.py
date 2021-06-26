from geometri.parent_geometry import ParentGeometry
from geometri.rectangle import Rectangle
from geometri.triangle import Triangle

rectangle = Rectangle(8, 4)
print(rectangle.info())

print(f'Rectnngle Count Area is {rectangle.count_area()}')

triangle = Triangle(7, 10)
print(triangle.info())

print(f'Triangle Count Area is {triangle.count_area()}')

geometry = ParentGeometry()
print(geometry.info())
print(geometry.count_area())
