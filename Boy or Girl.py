alphabet = "abcdefghijklmnopqrstuvwxyz"
name = input()

nameLen = 0
for letter in alphabet:
    if letter in name:
        nameLen += 1

if nameLen % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
