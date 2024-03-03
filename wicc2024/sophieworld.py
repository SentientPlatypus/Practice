n = int(input())
ideas = list(map(int, input().split()))
ideas.sort(key = lambda x: x * -1)

print(ideas)
#get the triplets
groups = []

smallest  = 10 ** 9
currenttriplet = []
for i in range(3, 2 * n + 4):
    d = ideas[i] - ideas[i + 2]
    if d < smallest:
        smallest = d
        currenttriplet = ideas[i: i + 3]

print(currenttriplet)
