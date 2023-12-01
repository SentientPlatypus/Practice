mygraph = {
    1: [3],
    3: [4, 2],
    4: [9],
    2: [1]
}

def shortestpath(start:int, end:int) -> int:
    queue = []
    distances = {}
    distances[start] = 0
    queue.append(start)
    
    if start == end:
        return 0

    while True:
        current = queue.pop(0)
        for node in mygraph[current]:
            queue.append(node)
            distances[node] = distances[current] + 1
            if node == end:
                return distances[node]
    return None


print(shortestpath(1, 9))



