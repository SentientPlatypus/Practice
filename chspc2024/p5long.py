N, M = list(map(int, input().split()))

L = []

for i in range(M):
    a, b = list(map(int, input().split()))
    L.append([a, b])



def generateLess(l:list):
    for i in range(len(l)):
        if l[i] == 0:
            continue

        s1, e1 = l[i]
        for k in range(len(l)):
            if i == k:
                continue
            if l[k] == 0:
                continue
            s2, e2 = l[k]

            if s2 <= e1 and e2 >= s1:
                l[i] = [min(s2, s1), max(e1, e2)]
                l[k] = 0
                break
    return l

L = [x for x in generateLess(L) if x != 0]


ans = 0
for a, b  in L:
    ans += abs(a - b)

print(N - ans)