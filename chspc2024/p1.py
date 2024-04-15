l = map(int, input().split())



m = {}
r = "YES"
for i in l:
    if i in m.keys():
        r = "NO"
    m[i] = 1

print(r)
