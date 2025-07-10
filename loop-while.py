count = 0
while(count < 3):
    print("HElloo World!!")
    count += 1
    
    # OR Single Line While loop
st = 2
while(st > 0): print("Vamsi",end = " "); print("Mandala"); st-=st   
    
    
li = [1,2,3,4]
revl = []
while li:
    revl.append(li.pop())    
print(revl)    


# While using break
s = "Geeks"
i = 0
while True:
    print(s[i])
    if s[i] == 'e' or s[i] == 's': break
    i += 1
print("Out of While loop")    