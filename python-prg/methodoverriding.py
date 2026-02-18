class A:
    def display(self):
        print("i belongs to class A")
class B(A):
    def display(self):
        print("i belongs to B")
b=B()
b.display()
