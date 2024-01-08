from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Adapted from : 3 Method's || C++ || JAVA || PYTHON || Beginner Friendly🔥🔥🔥
        => Time comolexity : O(n)
        => Space complexity: O(n)
        """
        traversed_elements = {}
        for ind in range(len(nums)):
            ele = nums[ind]
            component = target - ele
            if component in traversed_elements.keys():
                return [ind, traversed_elements[component]]
            else:
                traversed_elements[ele] = ind
        return [None]