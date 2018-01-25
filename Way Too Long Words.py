n = int(input())
for i in range(0, n):
    word = input()
    # print(word)
    if len(word) > 10:
        print(word[0] + (len(word) - 2).__str__() + word[len(word) - 1])
    else:
        print(word)
