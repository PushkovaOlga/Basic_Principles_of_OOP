
class RoboCat():
    def __init__(self, material, ears, hp):
        self.material = material
        self.ears = True
        self.hp = 9

    def meow(self):
        print("Мяу")
#Создание Объекта
robocat1 = RoboCat("Metal", True, str(8))
print(robocat1.hp)

class GreenRoboCat(RoboCat):
    def __init__(self, material, ears, superpower):
        super().__init__(material, ears, )
        self.superpower = superpower
        










