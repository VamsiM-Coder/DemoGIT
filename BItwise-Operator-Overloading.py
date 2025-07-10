class Change():
    def __init__(self,val):
        self.val = val
        
    def __and__(self,obj):
        print("AND Operator Overloaded")
        
        if isinstance(obj, Change):
            return self.val & obj.val
        else:
            raise ValueError("Must be a Object of class Change")
        
    def __or__(self,obj):
        print("OR Operator Overloaded")
        
        if isinstance(obj, Change):
            return self.val | obj.val
        else:
            raise ValueError("Must be a Object of class Change")        
    
    def __xor__(self,obj):
        print("XOR Operator Overloaded")
        
        if isinstance(obj, Change):
            return self.val ^ obj.val
        else:
            raise ValueError("Must be a Object of class Change")
        
    def __lshift__(self,obj):
        print("LEFT SHIFT Operator Overloaded")
        
        if isinstance(obj, Change):
            return self.val << obj.val
        else:
            raise ValueError("Must be a Object of class Change")    
        
    def __rshift__(self,obj):
        print("RIGHT SHIFT Operator Overloaded")
        
        if isinstance(obj, Change):
            return self.val >> obj.val
        else:
            raise ValueError("Must be a Object of class Change")    
        
    def invert(self):
        return ~self.val      
    
# Drivers code (It is the code that calls your classes, functions, or methods to run the program and see the output).
if __name__ == "__main__":
    a = Change(10)
    b = Change(20)
    print(a & b)
    print(a | b)
    print(a << b)
    print(a >> b)
    print(~a) 
    
'''
Operator overloading is not needed for basic programs, but it's very useful when:

Working with custom objects

You want intuitive syntax

You need validation or control

You aim for readable, maintainable, reusable code

'''    