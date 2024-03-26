x1, y1, x2, y2 = list(map(int, input().split()))

knightmoves = [
    [x1 + 1, y1 + 2],
    [x1 - 1, y1 + 2],
    [x1 + 1, y1 - 2],
    [x1 - 1, y1 - 2],
    [x1 + 2, y1 - 1],
    [x1 + 2, y1 + 1],
    [x1 - 2, y1 - 1],
    [x1 - 2, y1 + 1],
]

if abs(y2 - y1) == abs(x2 - x1):
    print("YES")
elif [x2, y2] in knightmoves:
    print("YES")
else:
    print("NO")

