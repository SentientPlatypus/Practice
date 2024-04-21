N, M, x, y = map(int, input().split())
grid = [input() for _ in range(N)]


#Sliding Window
fl = []
for r in range(N - x + 1):
    for c in range(M - y + 1):
        temp = ""
        for xi in range(x):
            for yi in range(y):
                temp += grid[r + xi][c + yi]
        fl.append(temp)

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

def gen_strength(s: str):
    checked = set()
    strength = 0
    for start in range(len(s)):
        for end in range(start + 1, len(s) + 1):
            substring = s[start:end]
            if checkorder(substring):
                strength += 1
    return strength

for i, fn in enumerate(fl):
    strength = gen_strength(fn)
    print(strength, end=" ")
    if (i + 1) % (M - y + 1) == 0:  # Print newline after each row
        print()