n = int(input())

x = 0
for i in range(0, n):
    if "++" in input():
        x += 1
    else:
        x -= 1

print(x)
