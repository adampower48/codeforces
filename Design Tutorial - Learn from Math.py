primes = list()


def primeSieve(bound):
    bound += 1
    numbers = [True] * bound

    for i in range(2, bound):
        if numbers[i]:
            for d in range(i * 2, bound, i):
                numbers[d] = False

    for i in range(2, bound):
        if numbers[i]:
            primes.append(i)


# Program starts
n = int(input())

primeSieve(n)

for i in range(4, n):
    if not (primes.__contains__(i) | primes.__contains__(n - i)):
        print("{} {}".format(i, n - i))
        break
