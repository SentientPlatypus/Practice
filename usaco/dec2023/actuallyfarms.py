testcases = int(input())

def solve():
    N = int(input())
    planth = list(map(int, input().split()))
    plantg = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if N == 1:
        print(0)
        return

    days = []


    for i in range(N):
        maxd = 0
        willbgreater = 0
        for k in range(N):
            if i == k:
                continue
            maxd = 0
            currentlygreater = planth[i] > plantg[k]
            if plantg[i] > plantg[k]:
                willbgreater += 1
            if plantg[i] > planth[k]:
                try:
                    maxd = max((planth[i] - planth[k]) / (plantg[k] - plantg[i]), maxd)
                    days.append(maxd)
                except:
                    pass
        if willbgreater != b[i]:
            print(-1)
            return

    print(max(days))


for i in range(testcases):
    solve()
        
        
