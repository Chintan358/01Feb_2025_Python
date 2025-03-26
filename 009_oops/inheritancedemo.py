
class A:

    _a = 20
    def show(self):
        print("Class A show mwthod calling",self._a)

class B(A):
    def disp(self):
        print("class B disp method calling",self._a)
class C(A):
    pass


b  = B()
a = A()
# b._a = 60
# b.disp()



print(dir(a))