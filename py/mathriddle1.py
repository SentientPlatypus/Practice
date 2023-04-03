
count = 0
for i in range(501):
    numstring = str(i)
    for substr in numstring:
        if substr == "1":
            count +=1

print(count)