n, t = map(int, input().split())
line = input()

for i in range(0, t):
    line = line.replace("BG", "GB")

print(line)
