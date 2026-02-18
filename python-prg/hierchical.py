class parent:
    def manners(self):
        print("my manners")
class firstchild(parent):
    def first(self):
        print("first")
class twochild(parent):
    def two(self):
        print("hero")
f=firstchild()
t=twochild()
f.first()
f.manners()
t.two()
t.manners()
