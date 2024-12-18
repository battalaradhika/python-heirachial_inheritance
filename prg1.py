#heirarchial inheritance
class A:
   def x(self):
        print("from x method of base class")
class B(A):
    def y(self):
        print("from y method of derived class")
class C(A):
    def z(self):
        print("from z method of derived class")

b=B()
b.x()
b.y()
c=C()
c.x()
c.z()