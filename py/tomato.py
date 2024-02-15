def neighbors(row, col, box) -> list[int]:
	return [[r, c] for r, c in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)] if r >= 0 and r < len(box) and c >= 0 and c < len(box[0]) and box[r][c] == 0]

def newmin(box):
	M, N = len(box), len(box[0])
	q = []
	visited = []
	for i in range(M):
		for j in range(N):
			if box[i][j] == 1:
				q.append([i, j])
	
	days = 0
	while True:
		toappend = []
		changed = False
		while q:
			current = q.pop(0)
			visited.append(current)

			r, c = current
			changed = True
			box[r][c] = 1
			
			neighborhood = neighbors(r, c, box)
			for neighbor in neighborhood:
				if neighbor not in visited:
					toappend.append(neighbor)
		
		all_ripe = True
		for i in range(M):
			for j in range(N):
				if box[i][j] == 0:
					all_ripe = False
					break
		if all_ripe:
			return days
	
		days += 1

		if not changed:
			return -1
		
		for cell in toappend:
			q.append(cell)


def read_box():
	M, N = list(map(int, input().split()))
	box = []
	for i in range(N):
		row = list(map(int, input().split()))
		box.append(row)
	return box

def print_box(box):
	for row in box:
		print(*row, sep=" ")

box = read_box()
days = newmin(box)
print(days)