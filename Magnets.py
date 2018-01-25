n = int(input())

groups = 0
last = ""

for i in range(0, n):
    magnet = input()
    if not magnet == last:
        groups += 1
        last = magnet

print(groups)
