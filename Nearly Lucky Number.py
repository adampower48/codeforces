number = input()
luckies = "47"

luckyDigits = 0
for digit in number:
    if luckies.__contains__(digit):
        luckyDigits += 1

if luckies.__contains__(str(luckyDigits)):
    print("YES")
else:
    print("NO")
