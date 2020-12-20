from graphics import Point
class Node:

    def __init__(self, name: str, point: Point=None) -> None:
        self.name = name
        self.point = point

    def __hash__(self):
        return hash(self.name)
    
    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if self.name == other.name:
            return True
        else:
            return False

    def set_pos(self, x: int, y: int) -> None:
        self.point = Point(x, y)

        
