n = int(input())
receivers = list(map(int, input().split()))

givers = [None] * n

for i in range(0, n):
    givers[receivers[i] - 1] = i + 1

out = " ".join(map(str, givers))
print(out)
