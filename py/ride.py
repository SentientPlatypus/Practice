"""
ID: geneust1
LANG: PYTHON3
TASK: ride
"""
fin = open ('ride.in', 'r')
fout = open ('ride.out', 'w')


comet = fin.readline()
group = fin.readline()

def getval(s:str) -> int:
    result = 1
    for c in s:
        result *= (ord(c) - ord('A') + 1)
    return result

if getval(comet) % 47 == getval(group) % 47:
    fout.write("GO\n")
else:
    fout.write("STAY\n")