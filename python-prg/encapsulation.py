class encap:
    __maxspeed=200
    def __init__(self):
        self.__updatespeed()
    def drive(self):
        print("im driving")
        print(self.__maxspeed)
    def __updatespeed(self):
        self.speed=100
        print(self.speed)

e=encap()
e.drive()
e.__maxspeed=500
'''it is not be called because it is private access modifier is
used and declared as instance variable'''

