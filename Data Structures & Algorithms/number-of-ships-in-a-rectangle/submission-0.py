# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea:
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point:
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution:
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        # First check: is there even a ship in this rectangle?
        if not sea.hasShips(topRight, bottomLeft):
            return 0
        
        # Base case: single point with a ship confirmed
        if topRight.x == bottomLeft.x and topRight.y == bottomLeft.y:
            return 1
        
        # Split into 4 quadrants
        mid_x = (topRight.x + bottomLeft.x) // 2
        mid_y = (topRight.y + bottomLeft.y) // 2
        
        return (
            self.countShips(sea, Point(mid_x, mid_y), bottomLeft) +                    # bottom-left
            self.countShips(sea, topRight, Point(mid_x + 1, mid_y + 1)) +              # top-right
            self.countShips(sea, Point(mid_x, topRight.y), Point(bottomLeft.x, mid_y + 1)) +  # top-left
            self.countShips(sea, Point(topRight.x, mid_y), Point(mid_x + 1, bottomLeft.y))    # bottom-right
        )