N = int(input())

grid = []
for i in range(N):
    grid.append(list(map(int,input().split())))


total  = 0
for r in range(N):
    for c in range(N):
        if r == c:
            continue
        total += grid[r][c]


print(total)