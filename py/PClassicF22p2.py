def parseinput():
    t = int(input())
    string = input()
    indexToRotateAround = int(input())
    return t, string, indexToRotateAround


def rotate(s:str, left=True) -> str:
    if left:
        firstchar = s[0]
        s += firstchar
        return s[1:]
    else:
        s = s[-1] + s
        return s[: -1]

    

def rotateString(s:str, r:int) ->str:
    left = s[:r]
    right = s[r + 1:]

    if left:
        left = rotate(left, True)
    if right:
        right = rotate(right, False)
    

    

    print(left + s[r] + right)









if __name__ == "__main__":
    t, string, indexToRotateAround = parseinput()
    rotateString(string, indexToRotateAround)
