class Vector2:

    def __init__(self, x:float, y:float):
        """
        Vector2.x = x

        Vector2.y = y

        returns (x, y)
        """
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return str((self.x, self.y))
    
    def __str__(self) -> str:
        return str((self.x, self.y))

    def max(self) -> int:
        if self.x > self.y : return self.x
        if self.x < self.y : return self.y
        return None
    
    def min(self) -> int:
        max = self.max()
        if max != None:
            if max == self.x:
                return self.y
            return self.x
        return None
