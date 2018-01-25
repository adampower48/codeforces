k = int(input())
l = int(input())
m = int(input())
n = int(input())
dragons = int(input())

smacked = 0

for d in range(1, dragons + 1):
    if min(d % k, d % l, d % m, d % n) == 0:
        smacked += 1
print(smacked)
