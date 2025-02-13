
words = "sun Rises in east"

print(words.capitalize())
print(words.casefold())
print(len(words))
print(words.center(19,'*'))
print(words.count('s',0,7))
print(words.endswith('es',0,9))
print(words.startswith('S',0,2))
print(words.find('k',3,9))   #if not found, return -1
print(words.index('k',3,9)) # if not found return valueError
