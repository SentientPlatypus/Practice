class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        N = len(s)  # s is the same length as target
        freqs = Counter(s)
        print(freqs)

        # sweep through target
        p = 0
        while p < N:
            if target[p] in freqs and freqs[target[p]] > 0:
                freqs[target[p]] -= 1
                if freqs[target[p]] == 0:
                    del freqs[target[p]]
            else:
                break
            p += 1

        # at this point in the code, i is at the index of the first differing character.
        for i in range(p, -1, -1):
            if i < N:
                candidates = [c for c in freqs if c > target[i]]

                if candidates:
                    best = min(candidates)
                    freqs[best] -= 1

                    rest = ""
                    for k in sorted(freqs.keys()):
                        rest += k * freqs[k]
                    
                    return target[:i] + best + rest
            if i > 0:
                freqs[target[i - 1]] += 1
        
        return ""
        
