acronym = input("Enter a full word acronym: ")
a_list = acronym.split()
sep = ""
for i in a_list:
    sep += i[0]

print(sep.upper())
print(type(sep))