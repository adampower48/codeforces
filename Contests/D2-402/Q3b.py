class Item:
    def __init__(self, w1, w2):
        self.w1 = w1
        self.w2 = w2
        self.change = w2 - w1


n, k = map(int, input().split())
week1 = list(map(int, input().split()))
week2 = list(map(int, input().split()))

items = list()
for i in range(0, n):
    items.append(Item(week1[i], week2[i]))

print(items)
items.sort(key=lambda x: x.change)
