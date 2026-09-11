class Solution:
    def isPalindrome(self, s: str) -> bool:
        s3=s.replace(" ","").lower()
        s1="".join(ch for ch in s3 if ch.isalnum())
        s2=""
        for i in range(len(s1)-1,-1,-1):
            s2+=s1[i]
        if s1==s2:
            return True
        return False