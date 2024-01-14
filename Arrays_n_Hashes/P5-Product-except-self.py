# Link : https://leetcode.com/problems/product-of-array-except-self/

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Approach - Use postfix & prefix product once 
        => Time complexity  : O(n)
        => Space complexity : O(n)
        """
        ## First approach : created a double loop O(n**2)
        # product = []
        # for i in range(len(nums)):
        #     p = 1
        #     for  j in range(len(nums)):
        #         if j !=i:
        #             p*=nums[j]
        #     product.append(p)
        # return product
        # counter = {}

        ## Second approach : optimized the double loop O(n**2)
        # for ele in nums:
        #     counter[ele] = counter.get(ele,0) +1

        # product = []
        # for ele in nums:
        #     p = 1
        #     for obj in counter:
        #         if ele != obj:
        #             p = p * (obj ** counter[obj])
        #         else:
        #             if counter[obj]>1:
        #                 p = p * (obj ** (counter[obj]-1))
        #     product.append(p)
        
        # return product

        # Third Approach : Inpired by solutions
        
        n = len(nums)
        answer = [1]*n

        for i in range(1, n):
            answer[i] = answer[i-1] * nums[i-1]
        
        prefix = 1
        for i in range(n-1,-1,-1):
            answer[i] *= prefix
            prefix *= nums[i]
        
        return answer
