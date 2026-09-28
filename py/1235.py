import bisect
class Solution:
    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        jobs = list(zip(startTime, endTime, profit))
        jobs.sort(key = lambda x: x[1])
        end_times = [j[1] for j in jobs]

        N = len(jobs)
        memo = {}

        def M(i):
            if i < 0:
                return 0

            if i in memo:
                return memo[i]
            
            prev = bisect.bisect_right(end_times, jobs[i][0]) - 1
            
            include = M(prev) + jobs[i][2]
            exclude = M(i - 1)

            memo[i] = max(include, exclude)
            return memo[i]
        
        return M(N - 1)

    def jobSchedulingTab(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        jobs = list(zip(startTime, endTime, profit))
        jobs.sort(key = lambda x: x[1])
        end_times = [j[1] for j in jobs]

        N = len(jobs)
        res = 0
        dp = [0] * (N + 1)

        for i in range(1, N + 1):
            s, e, p = jobs[i - 1]

            prev = bisect.bisect_right(end_times, s) - 1
            include = dp[prev + 1] + p
            exclude = dp[i - 1]
            dp[i] = max(include, exclude)
        
        return dp[N]
