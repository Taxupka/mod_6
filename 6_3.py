import random

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0
    def __init__(self, speed):
        self.speed = speed
        self._cords = [0, 0, 0]


    def move(self, dx, dy, dz):
        self._cords[0] = dx * self.speed
        self._cords[1] = dy * self.speed
        if dz * self.speed < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords[2] = dz * self.speed


    def get_cords(self):
        print(f'X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}')


    def attack(self):
        if self._DEGREE_OF_DANGER >= 5:
            print(f"Be careful, i'm attacking you 0_0")
        else:
            print(f"Sorry, i'm peaceful :)")



class Birds(Animal):
    beak = True


    def lay_eggs(self):
        eggs = random.randint(1, 4)
        print(f"Here are(is) {eggs} eggs for you")


class Aquatic_animal(Animal):
    _DEGREE_OF_DANGER = 3


    def dive_in(self, dz):
        dz = abs(dz)
        if dz:
            self._cords[2] = int(self._cords[2] - dz / 2 * self.speed)


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8


class Duckbill(PoisonousAnimal, Birds, Aquatic_animal):

    sound = "Click-click-click"

    def speak(self):
        print(self.sound)



db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()





