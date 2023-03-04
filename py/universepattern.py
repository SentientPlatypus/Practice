def parse(s:str):
    m = ["1"]
    vals = [s[0]]

    for x in range(1, len(s)):
        current = s[x]
        prev = s[x - 1]

        if current == prev:
            m[-1]  = str(int(m[-1]) + 1)
        else:
            m.append("1")
            vals.append(current)
    return ''.join(vals + m)


def solution(n):
    if n == 1:
        return "42"
    return parse(solution(n - 1))

n = int(input())
print(solution(n))
