# membership operator (tuple,lisr,strings)
''' in operator: Evaluates TRUE if variable present in sequence '''
''' not in operator: Evaluates TRUE if variable is not present in sequence'''

if('A' in 'Dedeepya'):
    print('True')
else:
    print("False")  
    
print('a' in 'Jashwanth')     

l1 = [1,2,3,4,5]
l2 = [5,6,7,8,9]

for item in l1:
    if item in l2:
        print("Overlapping")
    else:
        print("Not Overlapping")    

print()        

# identity operator (It is used to compare the objects (having same data type and share same memory location))
x = 5
y = 5
print(id(x))
print(id(y))

print(x is y)

y = 6
print(x is y)
