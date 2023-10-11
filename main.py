class RoboCat():
    def __init__(self, material, ears, hp):
        self.material = material
        self.ears = True
        self.hp = 9

    def meow(self):
        print("Мяу")

class GreenRobocat(RoboCat):
    def __init__(self, material, ears, superpower):
        super().__init__(material, ears)
        self.superpower = superpower 