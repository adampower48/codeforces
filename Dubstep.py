words = list(input().split("WUB"))

for i in range(0, words.count("")):
    words.remove("")

print(" ".join(words))
