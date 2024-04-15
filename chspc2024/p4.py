N, R, Q = list(map(int, input().split()))



def rev(l:list, a, b):
    reversedrange = l[a - 1:b]
    reversedrange.reverse()
    return l[:a - 1] + reversedrange + l[b:]

l = [k + 1 for k in range(N)]
o = [k + 1 for k in range(N)]



for i in range(R):
    a, b = list(map(int, input().split()))
    l = rev(l, a, b)


for i in range(Q):
    f = int(input())
    val = l[f - 1] #val at current is where in original
    print(val)

    

    











