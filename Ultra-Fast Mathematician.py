num1 = input()
num2 = input()

output = ""
for i in range(0, len(num1)):
    if num1[i] == num2[i]:
        output += "0"
    else:
        output += "1"

print(output)
