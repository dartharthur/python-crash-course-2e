# a string is a series of characters

name = "ada lovelace"
print(name.title()) # "Ada Lovelace"
print(name.upper()) # "ADA LOVELACE"
print(name.lower()) # "ada lovelace"

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}" # this is an f-string
print(full_name) # "ada lovelace"

# f is for format, because Python formats the strong by replacing the name of any variable 
# in braces with its value. Essentially, string interpolation.

print(f"Hello, {full_name.title()}!") # "Hello, Ada Lovelace!"

message = f"Hello, {full_name.title()}!"
print(message) # "Hello, Ada Lovelace!"

# note, if using Python 3.5 or earlier, will need to use the format() method

print("\tPython")
print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript")

favorite_language = " python "
favorite_language.rstrip() # " python"
favorite_language.lstrip() # "python "
favorite_language.strip() # "python"