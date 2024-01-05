# Link to Ques : https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Brute force approach : check if sorted string is same
        => Time Complexity : O(n *logn)
        => Space Complexity : O(1)
        """
        # s = list(s)
        # s.sort()
        # s = str(s)
        # t = list(t)
        # t.sort()
        # t = str(t)
        # if s==t:
        #     return True
        # else:
        #     return False
        """
        Hashmap based apprach : count of elements and then compare via dict
        => Time complexity : O(n)
        => Space complexity : O(n)
        """
        if len(s)!=len(t):
            return False
        s= self.string_to_dict(s)
        t= self.string_to_dict(t)
        if len(s)!=len(t):
            return False # is letters do not match
        else:
            for key in s:
                comparabale = t.get(key,0)
                if not comparabale:
                    False
                if s[key]!=comparabale:
                    return False
            return True
    
    def string_to_dict(self, l:str) -> dict:
        d = dict()
        for i in l:
            d[i] = d.get(i,0)+1
        return d
