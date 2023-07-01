#!/usr/bin/python3
""" Finds a peak inside a list """

def find_peak(list_of_integers):
    nums = list_of_integers
    if not nums:
        return None

    low = 0
    high = len(nums) - 1

    while low < high:
        mid = (low + high) // 2

        if nums[mid] < nums[mid + 1]:
            low = mid + 1
        else:
            high = mid

    return nums[low]
