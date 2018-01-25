s = input()

if "+" not in s:
    print(s)
else:
    s = s.split("+")
    s.sort()

    out = s[0]
    for i in range(1, len(s)):
        out += "+{}".format(s[i])

    print(out)
