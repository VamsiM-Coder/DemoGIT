def func():
    print("It is my First Function")
if __name__ == "__main__":
    func()    
    
# DEFAULT Argument - while function call for argument i passed one value but actually in actual functional parameters have two one is assigned with default value.
def myFun(x, y =20):
    print("x:",x)
    print("y:",y)
if __name__ == "__main__":
    myFun(10)        
    
# Keyword Arguments - Allow the caller to specify the agument name with values so that caller does not remember order of parameters.
def student(fn,ln):
    print(fn,ln)
if __name__ == "__main__":
    student(fn = "hello",ln = "world")    
    student(ln = "world", fn = "hello")


   