class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        argument={}
        for i in range(len(strs)):
            sort_word = "".join(sorted(strs[i]))
            if sort_word in argument:
                argument[sort_word].append(strs[i])
            else:
                argument[sort_word]=[strs[i]]
        return list(argument.values())