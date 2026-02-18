#hybird
class animal:
    def sound(self):
        print("make asound")
class cat(animal):
    def make(self):
        print("meow meow")
class dog(animal):
    def make_1(self):
        print("bow bow")
class hybrid(cat,dog):
    def hybird_s(self):
        print("i can play music")
h=hybrid()
h.hybird_s()
h.make_1()
h.make()
h.sound()
