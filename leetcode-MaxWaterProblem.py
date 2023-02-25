

def maxArea(height):
    def getCoords(n:list):
        fullcoords = []
        for x in range(len(n)):
            fullcoords.append((x+1, n[x]))
            print((x+1, n[x]))
        return fullcoords

    def getArea(coord1, coord2):
        return abs((coord2[0]-coord1[0])) * min(coord1[1], coord2[1])

    Coordinates = getCoords(height)
    maxArea = 0

    firstIndex = 0
    lastIndex = len(Coordinates)-1

    while firstIndex < lastIndex:

        maxArea = max(maxArea, getArea(Coordinates[firstIndex], Coordinates[lastIndex]))

        if Coordinates[firstIndex][1] >= Coordinates[lastIndex][1]:
            lastIndex -= 1
        else:
            firstIndex +=1
    
    return maxArea


print(maxArea([2,3,4,5,18,17,6]))
