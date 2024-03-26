n = input()
record = input()

smap = {
    "*": 100,
    "o": 50,  
    "x": 0
}

score = 0
combo = 0
prev = 0
for i in record:
    score += smap[i]
    if i == "*" or i == "o":
        score += combo
        combo += 1
    if i == "x":
        combo = 0

    
print(score)

