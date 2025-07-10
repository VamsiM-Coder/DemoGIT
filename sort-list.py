li = [5,3,2,1,4]

# It modifies original list
li.sort()
print(li)

li2 = [7,2,5,8,3]
# It returns a new list : Doesn't modify the original list
print(sorted(li2))
print(li2)

li3 = [6,3,7,8,2]
# It sorts in reverse order (Descending Order)
li3.sort(reverse = True)
print(li3)

words = ["apple","fig","banana","kiwi"]
# Sort with length of word
words.sort(key = len)
print(words)

pairs = [
    (1,'b'),
    (2,'a'),
    (3,'c')
]
# Sorting tuples by 2 nd value
print(sorted(pairs, key = lambda x : x[1]))