def parse():
    t = int(input())
    nmonsters = int(input())
    monsters = list(map(int, input().split()))
    nRequiredForFusing = int(input())


    return t, nmonsters, monsters, nRequiredForFusing

def monsterMash(m:list, n) -> list:
    i = 0
    while i < len(m):
        k = i + 1
        count = 1
        while k < len(m) and m[k] == m[i]:
            count += 1
            k += 1


        if count >= n:
            for k in range(min(n, count)):
                m.pop(i)
            i = 0
        else:
            i += 1
    print(m)
        






if __name__ == "__main__":
    t, nmonsters, monsters, nRequiredForFusing = parse()
    monsterMash(monsters, nRequiredForFusing)