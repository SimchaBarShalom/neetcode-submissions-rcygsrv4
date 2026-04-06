class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str1= [0]*26
        str2= [0]*26
        for i in range (len(s)):
            char=s[i]
            str1[ord(char) - ord('a')] +=1
        for i in range (len(t)):
            char=t[i]
            str2[ord(char) - ord('a')] +=1
        for i in range (len(str1)):
            if str1[i] != str2[i]:
                return False
        return True

   