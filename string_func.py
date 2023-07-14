rand_string = "    this is an important string    "
#This function removes whitespace on the left
rand_string = rand_string.lstrip()
#This function removes whitespace on the right
rand_string = rand_string.rstrip()
#This function removes whitespace on both sides
rand_string = rand_string.strip()

#capitalize
print(rand_string.capitalize())
print(rand_string.upper())
print(rand_string.lower())

a_list = ["Bunch", "of", "random", "words"]
print(" ".join(a_list))

#create a list from a string
a_list_2 = rand_string.split()
for i in a_list_2:
    print(i, end=" ")
print()
print(type(a_list_2))

#Count how many times a string appears in a string
print("How many i :", rand_string.count("i"))

#get index of matching string
print("Where is string :", rand_string.find("string"))
#Replace a string
print(rand_string.replace("an ", "a kind of "))

#Function to find out the type of strings

letter_z = "z"
num_3 = "3"
a_space = " "

print("Is z a letter or number :", letter_z.isalnum())
print("Is z a letter :", letter_z.isalpha())
print("Is 3 a number :", num_3.isdigit())
print("Is z a lowercase :", letter_z.islower())
print("Is z a uppercase :", letter_z.isupper())
print("Is space a space :", a_space.isspace())
