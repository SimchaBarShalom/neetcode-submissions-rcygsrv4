class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        hash_map=Counter(candidates)
        unique_list=list(hash_map.keys())
        def combinationSum(index,target,combination):
            if target==0:
                res.append(combination.copy())
                return
            if index>=len(unique_list):
                return
            num=unique_list[index]
            if hash_map[num]>0 and target>=num:
                combination.append(num)
                hash_map[num]-=1
                combinationSum(index,target-num, combination)
                hash_map[num]+=1
                combination.pop()
            combinationSum(index+1,target,combination)
        combinationSum(0,target,[])
        return res