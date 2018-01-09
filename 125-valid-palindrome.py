#EASY
# The tricky part is to do this task only in one pass
# If you want to do it in 2 passes then you will get timeout.
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == "":
            return True
        j = len(s)-1
        i = 0

        while i < j:
            if not s[i].isalnum():
                i += 1
                continue
            if not s[j].isalnum():
                j -= 1
                continue
            if s[i].lower() != s[j].lower():
                return False
            else:
                i+=1
                j-=1

        return True 
