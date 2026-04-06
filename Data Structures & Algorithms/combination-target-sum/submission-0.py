class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]

        def combination(i,num,curr):  
            if num==0:
                res.append(list(curr))
                return 
            if num<0 or i==len(nums):
                return
            combination(i,num-nums[i],curr+[nums[i]])
            combination(i+1,num,curr)
        combination(0,target,[])
        return res