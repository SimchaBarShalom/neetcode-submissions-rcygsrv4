class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]

        def subres(i,current):
            if i==len(nums):
                res.append(list(current))
                return 
            subres(i+1,current)
            subres(i+1,current+[nums[i]])
        subres(0,[])
        return res
        
        