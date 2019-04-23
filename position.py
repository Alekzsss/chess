class Position:
    def __init__(self, coordinates, color):
        self.x = coordinates[0]
        self.y = coordinates[1]
        self.color = color
        self.resident = None