class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        maxcount = 0
        maxnum = arr[0]

        current = arr[0]
        timesappeared = 0
        for i in arr:
            if i == current:
                timesappeared += 1
            else:
                if timesappeared > maxcount:
                    maxcount = timesappeared
                    maxnum = current
                timesappeared = 1  # Reset the counter for the new number
                current = i

        # Check one more time after the loop ends
        if timesappeared > maxcount:
            maxnum = current

        return maxnum

        