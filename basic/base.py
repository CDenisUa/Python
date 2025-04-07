
list_data = [1, 'abc', True]
tuple_data = (1, 2, 3)
set_data = {1, 2, 3, 3}
dict_data = {'a': 1, 'b': 2, 'c': 3}



# Input global function
name = input('Enter your name: ')


# Conditions
if name.isdigit():
    print(25 + int(name))
elif isinstance(name, str) :
    print(name.upper())
else:
    print(name)


# For loops
for listItem in list_data :
    print(listItem)

for tupleItem in tuple_data :
    print(tupleItem)

for key, value in dict_data.items() :
    print(key, value)

for key in dict_data.keys() :
    print(key)

for key in dict_data.values() :
    print(key)