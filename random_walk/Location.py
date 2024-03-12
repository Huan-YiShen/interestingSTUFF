''' can inherit from object'''

class RW_Location():
    def __init__(self, x : float, y : float):
        self.x = x
        self.y = y
    
    def move(self, deltaX : float, deltaY : float):
        ''' immutable '''
        return Location(self.x + deltaX, self.y + deltaY)

    def get_x(self):
        return self.x


    def get_y(self):
        return self.y


    def distTo(self, other):
        dx = self.x - other.get_x()
        dy = self.y - other.get_y()

        return (dx**2 + dy**2)**0.5


    def __str__(self):
        return "Location: ("+ str(self.x) + ", "\
             + str(self.y) + ")"