# Link to Ques : https://leetcode.com/problems/two-sum
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Brute Force - sort the list and traverse
        => Time comolexity : O(n*logn)
        => Space complexity: ??
        """
        f = sorted(nums)
        i =0
        j=1
        is_i = False
        while f[i]+f[j] != target:
            if f[i]+f[j] < target:
                if j < len(f)-1:
                    j+=1
                elif i < j-1:
                    i+=1
            else:
                if not is_i:
                    i+=1
                    is_i = not is_i
                else:
                    j+=1
                    is_i = not is_i
                # elif j-i > 1:
                #     j-=1
        try:
            return [nums.index(f[i]),i+1+nums[i+1:].index(f[j])]
        except:
            return [nums.index(f[i]), nums.index(f[j])]