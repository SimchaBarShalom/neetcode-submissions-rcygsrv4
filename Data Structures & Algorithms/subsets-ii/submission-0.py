class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def subset(i,curr,flag):
            if i==len(nums):
                res.append(curr.copy())
                return
            subset(i+1,curr,False)
            if i == 0 or nums[i]!=nums[i-1] or flag:
                curr.append(nums[i])
                subset(i+1,curr,True)
                curr.pop()
        subset(0,[],True)
        return res