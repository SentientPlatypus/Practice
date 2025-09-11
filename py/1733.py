class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        lset = {i + 1: set(languages[i]) for i in range(0, len(languages))}
        #lset[i] returns the languages person i knows

        problems = [[x,y] for x,y in friendships if lset[x] & lset[y] == set()]

        if not problems:
            return 0


        res = 9999999
        for i in range(1, n + 1):
            teach = set()
            for x,y in problems:
                if i not in lset[x]:
                    teach.add(x)
                if i not in lset[y]:
                    teach.add(y)
            res = min(res, len(teach))


        #why does this work? lets say person a is friends with both b and c. if b and c have a common language, then a only needs to learn one language.
        # what if there is another person c who is in the same predicament with his friends d and e? if d and e have a common language, then c only needs to learn one language.
        # doesnt this universal language only work for one group of friends?
        return res