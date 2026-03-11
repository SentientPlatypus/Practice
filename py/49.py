class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cores = {}

        for s in strs:
            srted = "".join(sorted(s))
            if srted in cores.keys():
                cores[srted].append(s)
            else:
                cores[srted] = [s]
        print(cores)
        return [cores[k] for k in cores.keys()]

        
