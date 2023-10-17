class RoboCat:
    def __init__(self, speed, sound, color):
        self.ears = 2
        self.hp = 9
        self.speed = speed
        self.sound = sound
        self.color = color

    def play_sound(self):
        print(f"Мой робокот говорит {self.sound}")


class AngryRoboCat(RoboCat):
    def __init__(self, speed, hp, color):
        super().__init__(speed, hp, color)
        self.superpower = "стрелять лазерами из глаз"

    def take_damage(self, damage):
        self.hp -= damage
        print(f"Осталось {self.hp}")

# my_robocat = RoboCat(10, "meow", "blue")
# print(my_robocat.ears)
# my_robocat.play_sound()
angry = AngryRoboCat(100,9, 'red')
angry.take_damage(2)


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