from geometri.parent_geometry import ParentGeometry

class Rectangle(ParentGeometry):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def info(self):
        return f'This Rectangle is width: {self.width} and height: {self.height}'

    def count_area(self):
        return self.width * self.height