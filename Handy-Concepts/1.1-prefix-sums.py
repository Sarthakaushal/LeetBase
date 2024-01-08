# Description : A prefix sum is a array containing sum of all pervious elements
# from any element in the array
from typing import List

def prefix_sum(l:List) -> List:
    array_list = [0 for i in range(len(l))]
    is_first = True
    index = 0
    for item in l:
        if is_first:
            array_list[index] = item
            is_first = not is_first
        else:
            array_list[index] = array_list[index-1] + l[index]
        index+=1
    return array_list

if __name__ == '__main__':
    n  = list(range(12, 40))
    p_sum = prefix_sum(n)
    print(f"\nList = {n}\nPrefix List = {p_sum}")
    