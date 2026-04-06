class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
     s={}
     for i in range(len(nums)):
        sub=target-nums[i]
        if sub in s:
            return [s[sub],i]
        s[nums[i]] = i
     return []