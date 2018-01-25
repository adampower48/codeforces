moves = 0

for i in range(0, 5):
    line = input()
    if line.__contains__("1"):
        moves += abs(2 - i)
        line = line.split(" ")
        moves += abs(2 - line.index("1"))
        break

print(moves)
