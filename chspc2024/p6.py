N, M, x, y = list(map(int, input().split()))


grid = []
for i in range(N):
    v = []
    st = input()
    for s in st:
        v.append(s)
    grid.append(v)

# print(grid)

nf = (N-x+1) * (M-y+1) # number of functions

funcList = []
outputs = []


for r in range(N - x + 1):
    for c in range(M - y + 1):
        temp = ""
        for xi in range(x):
            for yi in range(y):
                temp += grid[r + xi][c + yi]
        funcList.append(temp)

def findCode(str):
    C = False
    O = False
    D = False
    E = False
    for letter in range(len(str)):
        if (str[letter] == "c"):
            C = True
        if (str[letter] == "o"):
            O = True
        if (str[letter] == "d"):
            D = True
        if (str[letter] == "e"):
            E = True
    if (not(C and O and D and E)):
        return 0

    
def remove(l):
    for f in l:
        for letter in range(len(f)):
            if (f[letter] != "c" or f[letter] != "o" or f[letter] != "d" or f[letter] != "e"):
                lu = list(f)
                lu.pop(letter)
                strwithout = "".join(lu)


def checkorder(str):
    q = ["e", "d", "o", "c"]
    for i in range(len(str)):
        if q:
            if str[i] == q[-1]:
                q.pop(len(q) - 1)
        else:
            return True
    if q:
        return False
    return True

        



            



# for func in range(nf):

#     temp = ""
#     for xi in range(x):
#         for yi in range(y):
#             temp += grid[xi][yi]
        
#     funcList.append(temp)




print(checkorder("cocdec"))
# print(funcList)
# findCode(funcList)