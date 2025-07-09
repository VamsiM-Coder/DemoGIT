#Seperator
print("09","07","2025",sep= "||")

#Input Taking
x = input("Enter First Number :")
y = input("Enter Second Number :")
print(int(x) + int(y)) # 10 + 20 => 30 (concatenation)
print(int(x),int(y)) # 10 , 20 => 10 20
#print(x + int(y)) //Error
print(type(x))
print(type(int(x)))

# We use "None" to indicate that we don't know the value yet 
# (or)
# We didn't assign any value to this variable
z = None
print(z)
z = 10
print(z)

# In python there is no char type, if we want char you should create a single char string it "a" or 'a'.
str1 = 'a'
print(str1,type(str1))

str2 = "a"
print(str2,type(str2))

str3 = "ab"
print(str3,type(str3))

str4 = 'ab'
print(str4,type(str4))