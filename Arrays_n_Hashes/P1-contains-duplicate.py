# Link to Ques : https://leetcode.com/problems/contains-duplicate/


from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Approach 1 brute force
        => Check difference in the length of the list and the set
        => Time complexity  : O(n)
        => Space complexity : O(n)
        """
        if len(nums)!=len(list(set(nums))):
            return True
        else:
            return False
        """
        Approach 2 brute force
        => sort list then check for consecutive elements
        => Time complexity  : O(n*logn)
        => Space complexity : O(n)
        """
        
        # nums.sort()
        # for i in range(1,len(nums)):
        #     if nums[i-1] == nums[i]:
        #         return True
        # return False