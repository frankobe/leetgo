# Easy
# T: o(n)
# S: o(n)
class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        
        Let n be the answer, the minimum number of times A has to be repeated.
        For B to be inside A, A has to be repeated sufficient times such that it is at least as long as B (or one more), hence we can conclude that the theoretical lower bound for the answer would be length of B / length of A.
        Let x be the theoretical lower bound, which is ceil(len(B)/len(A)).
        The answer n can only be x or x + 1 (in the case where len(B) is a multiple of len(A) like in A = "abcd" and B = "cdabcdab") and not more. Because if B is already in A * n, B is definitely in A * (n + 1).
        Hence we only need to check whether B in A * x or B in A * (x + 1), and if both are not possible return -1.
        """
        x = int(math.ceil(1.0*len(B)/len(A)))
        if B in A*x:
            return x
        elif B in A*(x+1):
            return x+1
        else:
            return -1
