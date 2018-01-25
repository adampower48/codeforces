n = int(input())

if n % 2 == 1:
    answer = (n - 1) / 2 - n
else:
    answer = n / 2

print(int(answer))
