class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
     maxlength=0
     hash_table = {item: 0 for item in nums} 
     for num in nums:
        length=0
        while num in hash_table: 
                length+=1
                num = num+ 1
        maxlength=max(maxlength,length)
     return maxlength
