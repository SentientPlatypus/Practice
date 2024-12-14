

def pascal_level(n):
    if (n == 0):
        return [1]
    if (n == 1):
        return [1, 1]
    
    nextmid = []
    prev = pascal_level(n - 1)
    for i in range(1, len(prev)):
        nextmid.append(prev[i] + prev[i - 1])

        
    return [1] + nextmid + [1]




if __name__ == "__main__":
    n = int(input())
    print(pascal_level(n))
