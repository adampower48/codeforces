def gcd(aDivs, bDivs):
    for d in aDivs:
        if d in bDivs:
            return d
    else:
        return None


def getDivs(num):
    divs = list()
    for i in range(1, num + 1):
        if num % i == 0:
            divs.append(i)

    divs.reverse()
    return divs


a, b, n = map(int, input().split())

aList = getDivs(a)
bList = getDivs(b)
nList = getDivs(n)

turns = 1
while n > 0:
    if turns % 2 == 1:
        n -= gcd(aList, nList)
    else:
        n -= gcd(bList, nList)

    turns += 1
    nList = getDivs(n)

print(turns % 2)
