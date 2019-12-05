from typing import List
import random


def bubble_sort(numbers: List[int]) -> List[int]:
    # optimization 1: if gone through without swapping, its sorted, stop looping
    # optimization 2: each pass, the last element is always sorted, don't loop to it anymore.
  
    # loop through len(numbers) times
        # loop through and compare two elements at a time
            # if the two elements are out of order, swap them

    # return the sorted list            


print(bubble_sort([1, 2, 3, 4, 5]))
print(bubble_sort([5, 4, 3, 2, 1, 0]))
print(bubble_sort([random.randrange(100) for _ in range(10)]))
