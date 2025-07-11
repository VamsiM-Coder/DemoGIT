arr = [5, 1 ,1, 2, 3, 5]

arr.sort()
print(arr)

res = []
for i in range(0,len(arr)):
    if i < len(arr) - 1 and arr[i] != arr[i + 1]:
        res.append(len(arr)-i)
        
print(res)        