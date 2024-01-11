
my_map = {}
distances = {}

start = 0
queue = []
queue.append(0)
distances[0] = 0

while queue:
    current = queue.pop(0)
    for node in my_map[current]:
        distances[node] = distances[current] + 1
        if node not in distances.keys():
            queue.append(node)

    

