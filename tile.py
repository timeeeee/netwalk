# Each tile will have a north, south, east, west neighbors
# It's up to the board class to connect them all

class Tile:
    """Tile holds a tile, its current orientation, and references to
       its neighbors.
    """
    def __init__(self, connections):
        # connections is a list of 4 boolean values, indicating if the tile
        # has a connection going in the direction [north, east, south, west]
        self.connections = connections
        
        # Dictionary of neighbors, with cardinal direction keys
        self.neighbors = {}

        # Remember if this tile's placement has been guessed already
        self.placed = False

        # Rotation will change where the connections are, but not neighbors
        self.rotation = 0

    def check_direction(self, direction):
        

    def check(self):
        """Check if the tile's placement conflicts with any neighbors"""


    def rotate(self, times=1):
        self.rotation += times

    def unrotate(self, times=1):
        self.rotation -= times

    def north_connection(self):
        return self.connections[(0 - self.rotation) % 4]

    def east_connection(self):
        return self.connections[(1 - self.rotation) % 4]

    def south_connection(self):
        return self.connections[(2 - self.rotation) % 4]

    def west_connection(self):
        return self.connections[(3 - self.rotation) % 4]

