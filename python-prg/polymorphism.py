class cat:
    def sound(self):
        print("meow meow")
class dog:
    def sound(self):
        print("bow bow")
def make_sound(animaltype):
    animaltype.sound()

c=cat()
d=dog()
make_sound(c)
make_sound(d)
