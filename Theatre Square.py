x, y, l = map(int, input().split())

# print("{} {} {}".format(x, y, l))
if x % l != 0:
    x += l - x % l
if y % l != 0:
    y += l - y % l
# print("{} {} {}".format(x, y, l))

print(int((x * y) / (l * l)))
