class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()

        def combination(i,num,curr,flag):
            if num==0:
                res.append(curr)
                return 
            if num<0 or i==len(candidates):
                return 
            combination(i+1,num,curr,False)
            if(i>0 and candidates[i]==candidates[i-1] and not flag):
                return 
            combination(i+1,num-candidates[i],curr+[candidates[i]],True)
        combination(0,target,[],True)
        return res
        