class Solution:
    def get_price(self, hours:int):
        total = 0
        counter = 0
        while counter <= hours:
            if counter <= 1000:
                total += 7.633
            else:
                total += 9.259
            counter +=1
        
        return total
    
if __name__ == "__main__":
    hours:int = int(input())
    print(Solution().get_price(hours))
