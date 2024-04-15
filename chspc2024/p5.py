N, M = list(map(int, input().split()))

d = [1] * N

for i in range(M):
    a, b = list(map(int, input().split()))
    
    for i in range(a, b):
        d[i] = 0

print(sum(d))

