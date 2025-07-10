class _Base:
    def __init__(self):
        self._a = 10
class _Derived(_Base):
    def __init__(self):
        _Base.__init__(self)
        print("Calling protected member of base class: ", self._a) 
        self._a = 3
        print("Calling modifies protected member outside class :" , self._a)
        
ob1 = _Derived()
print("Accessing protected member of obj1: ", ob1._a)

ob2 = _Base()
print("Accessing protected member of obj2: ", ob2._a)
                       