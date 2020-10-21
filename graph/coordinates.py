"""Class: Coordinates"""

# class coord:
# 	def __init__(self, x,y):
# 		self.x=x
# 		self.y=y
#     def new_coord(self, dx,dy):
#         return coord(self.x+dx,self.y+dy)
#     def distance(self, coord2):
#         dist_x=self.x-coord2.x
#         dist_y=self.y-coord2.y
#         return (dist_x**2+dist_y**2)**0.5



class coord:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def new_coord(self, dx, dy):
        return coord(self.x + dx, self.y + dy)

    def distance(self, coord2):
        delta_x = self.x - coord2.x 
        delta_y = self.y - coord2.y 

        return (delta_x**2 + delta_y**2)**0.5     