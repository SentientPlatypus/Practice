n, a, b = list(map(int, input().split()))


t = 0

while 1:
    t += 1
    n = n - a

    if t % b == 0:
        a += 1
    if n <= 0:
        break

print(t)

