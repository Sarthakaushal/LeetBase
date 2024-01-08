from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Approach - sort string and put in hash then append hash list
        => Check difference in the length of the list and the set
        => Time complexity  : O(n*k*logk) -> k is the largest string in strs
        => Space complexity : O(n)
        """
        def sort_string(self, s:str)->str:
            s = list(s)
            return ''.join(sorted(s))

        def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            groups= {}
            for ele in strs:
                ele_sorted = self.sort_string(ele)      
                if ele_sorted in groups.keys():
                    value = groups.get(ele_sorted, [])
                    value.append(ele)
                else:
                    groups[ele_sorted] = [ele]
            
            result = []
            for value in groups.values():
                result.append(value)