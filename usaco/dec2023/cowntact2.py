N = int(input())

s = str(input())
i = 0
numsick = 0
totalsick = 0
isolated = False


while i < len(s):
    k = 0
    if s[i] == "1":

        totalsick += 1

        if (i == 0 and s[i + 1] == "0") or (i > 0 and i < len(s) - 1 and s[i + 1] =="0" and s[i - 1] == "0") or (i == len(s) - 1 and s[i - 1] == "0"):
            isolated = True


        if not isolated:
            while i + k < len(s) and s[i + k] == "1":
                k += 1
                if k > 1:
                    totalsick += 1
            if k % 2 == 0:
                numsick += 2
            else:
                numsick += 1
            i += k - 1
    i += 1

if isolated:
    print(totalsick)
else:
    print(numsick)