# we want to import the array module (It only supports for 1d array)
from array import array
arr = array('d',[1,2,3,4])
print(arr[0])

arl1 = [1,2,3,4]
print(arl1)

arl2 = [
    [1,2,3],
    [4,5,6]
]
arl2.append([7,8,9])

print(arl2)
