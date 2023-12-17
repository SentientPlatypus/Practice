N = int(input())

s = str(input())


import math


i = 0
numsick = 0
substrLength = []
isEdge = []
while i < len(s):
    if s[i] == "1":
        k = 0
        while i + k < len(s) and s[i + k] == "1":
            k += 1
        substrLength.append(k)
        if i == 0 or i + k == len(s) - 1:
            isEdge.append(1)
        else:
            isEdge.append(0)
        i += k - 1
    i += 1

if not substrLength:
    print("0")

else:
    
    minimumlocations = []
    shortestsubstr = min(substrLength)
    for i in range(len(substrLength)):
        if substrLength[i] == shortestsubstr:
            minimumlocations.append(i)

    nights = 0
    for i in minimumlocations:
        if not isEdge[i]:
            nights = (shortestsubstr - 1) // 2
            break
        else:
            nights = (shortestsubstr - 1)
    groups = 2 * nights + 1
    for l in substrLength:
        numsick += math.ceil( l / groups)

    print(numsick)
    

