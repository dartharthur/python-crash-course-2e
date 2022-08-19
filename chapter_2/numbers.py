# exponents
print(3 ** 2) # 9
print(3 ** 3) # 27
print(10 ** 6) #1000000

# python has:
# integers
# floats

# when you divide any two numbers, even integers that result in a whole number, you get a float
print(4/2) # 2.0

# mixing an integer and a float in any other operation also results in a float
# python defaults to a float in any operation that uses a float, even if the output is a whole number

# when writing long numbers, you can group digits using underscores to make large numbers more readable
universe_age = 14_000_000_000
print(universe_age)
# 1000 is the same as 1_000 or 10_00

# you can assign values to more than one variable using a single line
# you'll most often use this technique when initializing a set of numbers
x, y, z = 0, 0, 0

# a constant is a variable who value stays the same throughout the life of a program
# Python doesn't have built-in constant types, just represent it with an all-caps variable name
MAX_CONNECTIONS = 5000

print(5+3)
print(9-1)
print(2*4)
print(16/2)

fav_number = 28
print(f"My fav number is {fav_number}")
