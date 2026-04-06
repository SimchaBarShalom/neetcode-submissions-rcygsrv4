class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq=[0]*26
        start=0
        max_freq=0
        length=0
        for end in range (len(s)):
            index=ord(s[end]) - ord('A')
            freq[index]+=1
            max_freq=max(max_freq,freq[index])
            if ((end-start)+1)-max_freq > k:
                index=ord(s[start]) - ord('A')
                freq[index]-=1
                start+=1
            length=max(length,(end-start)+1)
        return length

    
        