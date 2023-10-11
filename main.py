
class Robocat():
    def __init__(self, material, ears, hp):
        self.material = material
        self.ears = True
        self.hp = 9
    def meow(self):
        print('meow meow, i am robocat')
robocat1 = Robocat('Metak', True, '9')
print (robocat1.material)
print(robocat1.hp)


class GreenRoboCat(RoboCat):
    def __init__(self, material, ears):
        super().__init__(material,ears)
        self.superpower = superpower