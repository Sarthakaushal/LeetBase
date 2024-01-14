# Link to Ques : https://leetcode.com/problems/top-k-frequent-elements/


from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Approach - Create a counter then use bucket sort
        => Check difference in the length of the list and the set
        => Time complexity  : O(n*k*logk) -> k is the largest string in strs
        => Space complexity : O(n)
        """
        counter = {}
        # k_freq = []
        # min_freq = 0
        
        # updating counter
        for ele in nums:
            counter[ele] = counter.get(ele, 0)+1
        
        if len(nums)==1:
            return nums
        # # 1) Use the Sorted func in python for nlog n
        # sorted_counter = sorted(counter, key=counter.get, reverse=True)
        # return sorted_counter[:k]
        
        # 2) Bucket sort : Maximum length can be nums.length

        mat = [ [] for x in range(len(nums)+1) ]
        for ele in counter:
            mat[counter[ele]].append(ele)
        
        output = []
        k_left = k
        is_done =False
        for i in range(len(nums),-1,-1):
            for ele in mat[i]:
                output.append(ele)
                k_left-=1
                if k_left==0:
                    is_done =True
                    break
            if is_done:
                break
        return output