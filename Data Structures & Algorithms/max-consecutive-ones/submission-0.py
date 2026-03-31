class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        max_ones = 0
        for num in nums:
            if num == 0:
                if counter > max_ones:
                    max_ones = counter
                
                counter = 0
            else:
                counter += 1
        
        if counter > max_ones:
            max_ones = counter
        
        return max_ones