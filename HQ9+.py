instructions = "HQ9"
s = input()

for inst in instructions:
    if s.__contains__(inst):
        print("YES")
        break
else:
    print("NO")
