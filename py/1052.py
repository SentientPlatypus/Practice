class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        l = 0
        grumpy_cust = sum(c for i, c in enumerate(customers) if grumpy[i])
        total_cust = sum(customers)
        
        res_compl = 0
        gcust = 0
        for r in range(len(customers)):
            curc = customers[r]

            if grumpy[r]:
                gcust += curc

            if r - l + 1 < minutes:
                continue
            
            # r - l + 1 == minutes
            res_compl = max(res_compl, gcust)
            if grumpy[l]:
                gcust -= customers[l]
            l += 1

        print(total_cust, res_compl)
        return total_cust - (grumpy_cust - res_compl)      

        
