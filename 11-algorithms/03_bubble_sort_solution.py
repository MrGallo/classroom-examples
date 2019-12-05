from typing import List
import random


def bubble_sort(numbers: List[int]) -> List[int]:
    # optimization 1: if gone through without swapping, its sorted, stop looping
    is_sorted = False

    # optimization 2: each pass, the last element is always sorted, don't loop to it anymore.
    times_through = 0

    while not is_sorted:
        is_sorted = True  # optimization 1
        # loop through and compare two elements at a time
        for i in range(len(numbers) - 1 - times_through):  # with optimization 2
            a = numbers[i]
            b = numbers[i+1]
            # if the two elements are out of order, swap them
            if a > b:
                numbers[i] = b
                numbers[i+1] = a
                is_sorted = False  # optimization 1
        times_through += 1  # optimization 2

    # return the sorted list
    return numbers
            


print(bubble_sort([1, 2, 3, 4, 5]))
print(bubble_sort([5, 4, 3, 2, 1, 0]))
print(bubble_sort([random.randrange(100) for _ in range(10)]))
