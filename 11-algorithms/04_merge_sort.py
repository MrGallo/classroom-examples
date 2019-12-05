from typing import List
import random

def merge_sort(numbers: List[int]) -> List[int]:
    # base case
    # find the midpoint
    # two recursive steps
    # mergesort left
    # mergesort right
    # merge the two together

    # loop through both lists with two markers
    # if right value less than left value, add right value to sorted, increase right marker
    # if left value less than right value, add left value to sorted, increase left marker

    # create a while loop to gather the rest of the values from either list
    
    # return the sorted list

print(merge_sort([1, 2, 3, 4, 5]))
print(merge_sort([5, 4, 3, 2, 1, 0]))
print(merge_sort([random.randrange(100) for _ in range(10)]))

