N, M = list(map(int, input().split()))

cows = list(map(int, input().split()))
canes = list(map(int, input().split()))


canerange = [[0, x] for x in canes]

for i in range(len(canes)):

    for k in range(len(cows)):
        if cows[k] > canerange[i][0]:
            
            if cows[k] > canerange[i][1]:
                difference = canerange[i][1] - canerange[i][0]
            else:
                difference = cows[k] - canerange[i][0]
            canerange[i][0] += difference
            cows[k] += difference


for cow in cows:
    print(cow)
    