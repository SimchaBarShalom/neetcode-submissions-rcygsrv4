class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_map={}
        max_length=0
        start=0
        for end in range (len(s)):
            c=s[end]
            if c in hash_map and hash_map[c]>=start:
                start=hash_map[c]+1
            hash_map[c]=end
            length=(end-start)+1
            max_length=max(max_length,length)
        return max_length


