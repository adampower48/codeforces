def doBitOperation(var1, var2, operation):
    output = ""

    if operation == "XOR":
        for k in range(0, len(var1)):
            if var1[k] == var2[k]:
                output += "1"
            else:
                output += "0"
    elif operation == "AND":
        for k in range(0, len(var1)):
            if var1[k] == "1" and var2[k] == "1":
                output += "1"
            else:
                output += "0"
    elif operation == "OR":
        for k in range(0, len(var1)):
            if var1[k] == "1" or var2[k] == "1":
                output += "1"
            else:
                output += "0"

    return output


n, bitDepth = map(int, input().split())

variables = dict()

variables["?"] = "".join(["0"] * bitDepth)

for i in range(0, n):
    line = input().split(" := ")
    variables[line[0]] = line[1]

print(variables)

for key in variables:
    if "AND" in variables[key] or "OR" in variables[key] or "XOR" in variables[key]:
        eqn = variables[key].split()
        variables[key] = doBitOperation(variables[eqn[0]], variables[eqn[2]], eqn[1])

print(variables)

print(bin(64)[2::])
print(int("100", 2))
