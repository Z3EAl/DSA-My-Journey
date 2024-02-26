""" this code uses 2 pointer technique to find if a word is palindrome or not. string consists on alphanumerical characters only.
    Time complexity is O(n) and space complexity is O(1)"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        res=""
        for i in s:
            if i.isalnum():
                res+=i.lower()
        if len(res)==0 :
            return True
        left=0
        right=len(res)-1
        while left<=right:
            if res[left]!=res[right]:
                return False
            else:
                left+=1
                right-=1
                continue
        
        return True