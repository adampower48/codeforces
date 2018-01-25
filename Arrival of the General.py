n = int(input())
soldiers = list(map(int, input().split()))

maxH = max(soldiers)
minH = min(soldiers)

maxMove = soldiers.index(maxH)
soldiers.reverse()
minMove = soldiers.index(minH)

moves = minMove + maxMove
if maxMove > len(soldiers) - 1 - minMove:
    moves -= 1

print(moves)
