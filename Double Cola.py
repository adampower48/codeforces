people = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
n = int(input())

for i in range(0, 32):
    if n > 5 * 2 ** i:
        n -= 5 * 2 ** i
    else:
        for k in range(0, 5):
            if n > 2 ** i:
                n -= 2 ** i
            else:
                print(people[k])
                break
        break
