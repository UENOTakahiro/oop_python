class Flower():

    picked = 0

    def __init__(self):
        self.color = "red"

    def pick(self):
        Flower.picked += 1

    def get_status(self):
        print( str(Flower.picked) + " flowers have been picked")
