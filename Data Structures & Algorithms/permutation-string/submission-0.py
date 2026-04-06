class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        freq_s1=[0]*26
        freq_s2=[0]*26
        for i in range(len(s1)):
            freq_s1[ord(s1[i])-ord('a')]+=1
            freq_s2[ord(s2[i])-ord('a')]+=1
        start=0
        for end in range (len(s1),len(s2)):
            if self.checkPermutation(freq_s1,freq_s2):
                return True
            freq_s2[ord(s2[end])-ord('a')]+=1
            freq_s2[ord(s2[start])-ord('a')]-=1
            start+=1
        return self.checkPermutation(freq_s1,freq_s2)

    
    def checkPermutation(self,freq_s1,freq_s2):
        for i in range(len(freq_s1)):
            if freq_s1[i]!=freq_s2[i]:
                    return False
        return True

            
            

    

     

        