class RoboCat():
    def __init__(self, material, ears, hp):
        self.material = material
        self.ears = True
        self.hp = 9

    def meow(self):
        print("мяу")

robocat1 = RoboCat("Mental", True, "9")
print(robocat1.material)

class GreenRoboCat(RoboCat):
    def __init__(self, material, ears, superpower):
        super().__init__(material, ears)
        self.superpower = superpower 