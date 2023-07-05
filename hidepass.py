norm_string = input("Enter a string to hide in uppercase: ")

secrete_string = ""

for char in norm_string:
    secrete_string += str(ord(char) - 23)

print("Secrete Message :", secrete_string)

norm_string = ""

for i in range(0, len(secrete_string) - 1, 2):
    char_code = secrete_string[i] + secrete_string[i + 1]
    norm_string += chr(int(char_code) + 23)

print("Original String :", norm_string)