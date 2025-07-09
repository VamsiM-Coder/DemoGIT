# list : We can dynamically add and remove items & Items are stored in contigous locations.
li = [10,10,20,30]
print(li)
li.append(40)
li.remove(10)
print(li)
print(type(li))

# tuple : It is also like a list, the difference is you can't modify once you created a tuple, these are immutable.
tup = (10,20,30)
print(tup)
print(type(tup))

# set : It is collection of items where all items are distnict and set is like mathematical set.
sett = {10,20,30}
print(sett)
print(type(sett))

# dictionary : It is used for mappings. This is a collection of key : value pairs.
dict = {10 : "vam", 20 : "si"}
print(dict)
print(type(dict)) #<class 'dict'>


s = "geeks"
print(list(s))
print(tuple(s))
print(set(s))
# print(dict(s)) It is not possible.


a = 20
print(bin(a))
print(hex(a))
print(oct(a))

