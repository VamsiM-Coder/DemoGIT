# range() return a sequence of numbers in a given range.
'''
   range(start, stop, step)
   
   start,step : optional
''' 

for _ in range(5): # stop
    print( _ , end =" ")
    
print()
    
for i in range(0, 5): # start,stop
    print(i, end = " ")    
    
print()

for i in range(0, 5, 1): # start, stop, step
    print(i,end=" ")    
    
print()    
    
# For loop (iterating over list)
str = "Geeks"
li = list(str)
for _ in li:
    print(_)    
    
    
# (iterating over dictionary)
print("Dictionary Iteration")
d = dict()
d['A'] = 65
d['B'] = 66
d['C'] = 67

for i in d:
    print("Key: %s Value: %d" %(i,d[i]))    
    
    
# For using break    
for char in str:   
    print(char) 
    if char == 'e' or char == 's':
        break
    
print()
    
# For using continue
for char in str:
    if char == 'e': continue
    else: print(char)
         