totalrabbits = 250000
day = 1

while True:
    for id in range(1, totalrabbits + 1):
        if id % 2 == day % 2:
            print("feed carrots")
        else:
            print("feed pizza")
    
    day += 1

