class Tile:
    def __init__(self, x, y, value):
        self._x = x
        self._y = y
        self._value = value
        self._revealed = False
        self._flagged = False
    
    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    @property
    def value(self):
        return self._value
    
    # you sneaky sneaky...
    @value.setter
    def value(self, value):
        if self._value == float('-inf'):
            self._value = value
    
    @property
    def revealed(self):
        return self._revealed
    
    @property
    def flagged(self):
        return self._flagged

    def reveal(self):
        if self._revealed == False:
            self._revealed = True
            if self._value != -1:
                return True
        return False
    
    def flag(self):
        if self._flagged == False:
            self._flagged = True
            return True
        return False
    
    def unflag(self):
        if self._flagged == True:
            self._flagged = False
            return True
        return False