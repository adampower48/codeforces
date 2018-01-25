hello = "hello"
word = input()

index = 0

for letter in word:
    if letter == hello[index]:
        if index == 4:
            print("YES")
            break
        index += 1
else:
    print("NO")
