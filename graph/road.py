
class road:
    def __init__(self):
        self.ant_coords={}
    def add_ant(self, ant, where):
        self.ant_coords[ant]=where
    def get_coordinates(self,ant):
        return self.ant_coords[ant]

    def move_ant(self,ant):
        delta_x, delta_y=ant.walk()
        # path_x.append(path_x[-1]+delta_x)
        # path_y.append(path_y[-1] + delta_y)
        coord_current=self.ant_coords[ant]
        new_coord=coord_current.new_coord(delta_x,delta_y)
        self.ant_coords[ant]=new_coord