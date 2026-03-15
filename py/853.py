class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        time_to_finish = []
        for i in range(len(position)):
            time_to_finish.append((target - position[i]) / speed[i])
        p_s = zip(position, time_to_finish)
        print(p_s)

        ps_sorted = sorted(p_s, key = lambda x: -x[0])
        print(ps_sorted)


        nfleets = 0
        max_time = 0
        
        for p, t in ps_sorted:
            if t > max_time:
                nfleets += 1
                max_time = t 
        return nfleets


