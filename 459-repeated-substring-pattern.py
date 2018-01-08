# O(N) time complexity
# O(1) space complexity
class Solution(object):
    def repeatedSubstringPattern(self, s):
        def shift(s, i):
            return s[i:]+s[0:i]
        """
        :type s: str
        :rtype: bool
        """
        for i in range(1, len(s)/2+1):
            if len(s)%i==0:
                ss = shift(s,i)
                if ss==s:
                    return True
        return False
