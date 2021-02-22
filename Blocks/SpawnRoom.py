from Blocks.Room import Room

class SpawnRoom(Room):

    def __init__(self, c_x, c_y, w, h):
        Room.__init__(self, c_x, c_y, w, h)

    def spawnHallway(self):
        
