# Variables

# Strings
name = 'Denys'
# Integer (Whole numbers)
integer = 10
# Float (decimal numbers)
float_number = 3.14
# Boolean
is_boolean = True | False

print('First symbol in name' + f' - {name}' , name[0])
print('Last symbol in name' + f' - {name}' , name[-1])

phrase = 'hello world'

print(phrase.upper())
print(phrase.lower())
print(phrase.capitalize())
print(phrase.replace('hello', 'world'))
print("world" in phrase)
print(len(phrase))


# Type conversion

age_str = '30'
age_num = int(age_str)
print(type(age_str))
print(type(age_num))

price_float = 29.99
price_int = int(price_float)
print(price_int)
print(type(price_float))
print(type(price_int))