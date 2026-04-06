class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        hash_map=Counter(candidates)
        unique_list=list(hash_map.keys())
        def combinationSum(index,target,path):
            if target==0:
                res.append(path.copy())
                return
            if index>=len(unique_list) or target<0:
                return
            num=unique_list[index]
            if hash_map[num]>0 and target>=num:
                path.append(num)
                hash_map[num]-=1
                combinationSum(index,target-num, path)
                hash_map[num]+=1
                path.pop()
            combinationSum(index+1,target,path)
        combinationSum(0,target,[])
        return res