#Acessing index values in strings
word = "Python, is a Programming Language"
for _ in range(len(word)): print(word[_])


#slicing
print(word[0:4]) # Pyth

#length of string
print(len(word)) # 32

#Upper function
print(word.upper()) # PYTHON IS A PROGRAMMING LANGUAGE

#Lower function
print(word.lower()) # python is a programming language

#Title function
print(word.title()) # Python Is A Programming Language

#Finding substrings in a string and returns start index of substring (-1 if not found)
print(word.find("Programming"))

#Finding substrings present or not 
print("Python" in word)

#Replacing Parts of String
print(word.replace("Python","Java"))

#Splitting the Strings
print(word.split(","))

#joining the text
print("-".join(word))

#Removing spaces begining and ending of the string
word1 = "   Java  is OOPS Language   "
print(word1.strip())