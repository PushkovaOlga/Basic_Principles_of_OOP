
class RoboCat():
    def __init__(self):
        self.health = 9
        self.material = "stall"
        self.ushi = True
    
    def INH(self):
        print("miau")

class GreenRoboCat(RoboCat):
    def __init__(self, material, health, ushi, super):
        super().__init__(material, ushi)


cat1 = RoboCat()
cat2 = GreenRoboCat()

cat1.health = 1

print(cat1.health)
print(cat2.health)
cat2.INH()