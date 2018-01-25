n, k = map(int, input().split())

n = str(n)

changes = 0
zeros = 0

for digit in n[::-1]:
    if zeros == k:
        break

    if digit == "0":
        zeros += 1
    else:
        changes += 1

if zeros != k:
    print(len(n) - 1)
else:
    print(changes)
