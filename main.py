class RoboCat():
    def __init__(self, material, ear, hp):
        self.material = material
        self.ears = True
        self.hp = 9

    def meow(self):
        print("Мяу")

#создание объекта
#obocat1 = RoboCat("Metal", True, str(8))
print(robocat.hp)


class GreenRobCat(RoboCat):
    def __init__(self, material, ears, superpower):
        super().__init__(materials, ears)
        self.superpower = superpower
