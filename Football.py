lineup = input()
dangerNum = 7

curPlayer = "x"
curCount = 0

for player in lineup:
    # print(curPlayer + " " + curCount.__str__() + ", new " + player)

    if player != curPlayer:
        curPlayer = player
        curCount = 1
    else:
        curCount += 1

    if curCount >= dangerNum:
        break

if curCount >= dangerNum:
    print("YES")
else:
    print("NO")
