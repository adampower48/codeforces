def genLuckies():
    tLuckies = []
    unluckies = ["1", "2", "3", "5", "6", "8", "9", "0"]
    for i in range(0, 1000):
        istr = str(i)
        for unlucky in unluckies:
            if istr.__contains__(unlucky):
                break
        else:
            tLuckies.append(i)

    return tLuckies


number = int(input())
luckies = genLuckies()

for luckyNum in luckies:
    if number % luckyNum == 0:
        print("YES")
        break
else:
    print("NO")
