N, R, Q = list(map(int, input().split()))



omp = {i + 1:i + 1 for i in range(N)} #original
mp = {i + 1:i + 1 for i in range(N)}




for i in range(R):
    a, b = list(map(int, input().split()))
    


    for k in range(a, b + 1):
        diff = k - a
        mp[k] = b - diff

for i in range(Q):
    f = int(input())

    print(omp[mp[f]])


