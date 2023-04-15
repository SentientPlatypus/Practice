class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        mv = [0] * (k + 1)
        pileSum = [0] * (k + 1)
        for pile in piles: # Iterate over each pile
            n = min(k, len(pile)) # Calculate the number of coins in the pile to consider
            sum = 0
            for i in range(1, n + 1):
                pileSum[i] = sum = sum + pile[i - 1] # Calculate the sum of coins taken from the pile for each possible number of coins
            for i in range(k, 0, -1): # Iterate over each possible number of coins
                maxVal = 0
                for j in range(min(i, n), -1, -1): # Iterate over each possible number of coins taken from the current pile
                    maxVal = max(maxVal, pileSum[j] + mv[i - j]) # Update the maximum total value of coins
                mv[i] = maxVal
        return mv[k] # Return the maximum total value of coins we can have in our wallet if we choose at most k coins from all the piles