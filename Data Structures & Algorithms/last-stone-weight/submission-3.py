class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max=100 
        counter = [0] * (max+1)
        for i in stones:
            counter[i] += 1 
        i = max
        while i > 0:
            if counter[i] == 0:
                i -= 1
                continue   
            counter[i] %= 2
            if counter[i] == 0:
                i -= 1
                continue  
            j = i - 1
            while j > 0 and counter[j] == 0:
                j -= 1 
            if j == 0:
                return i 
            counter[j] -= 1
            counter[i - j] += 1
            counter[i] -= 1
        return 0