# practice for loop
# ask user for name and count each character
# "Ankit Diwakar"
# A : 3
# n : 1
# k : 2
# i : 2
# t : 1
#   : 1
# D : 1

name = input("enter your name : ")
temp = ""
for i in range(len(name)):
    if name[i] not in temp:
        print(f"{name[i]}: {name.count(name[i])}")
        temp += name[i]