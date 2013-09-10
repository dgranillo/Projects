#!/usr/bin/env python2.7
"""
 Sorting - Implement two types of sorting algorithms: Merge sort and bubble
 sort.
 
 Author: Dan Granillo <dan.granillo@gmail.com>
 
 ToDo: Merge sort does not append remaining values from one half if the other's
 counter has reached the limit. Generally 2nd half's last number is ommitted.
 
 Bubble sort would be more efficient if instead of running max iterations,
 results were compared to originalList.sort()
 
"""

import random

def genNums(x, y):
    nums = [random.randrange(x, y) for i in range(20)]
    print 'Random: ', nums
    return nums

def mergeSplit(nums):
    half1 = [nums[i] for i in range(len(nums)/2)]
    half2 = [nums[i] for i in range(len(nums)/2, len(nums))]
    return (half1,half2)

def mergeConquer(halves):
    half1 = sorted(halves[0])
    half2 = sorted(halves[1])
    return (half1, half2)

def mergeCombine(halves):
    mergedNums = []
    half1 = halves[0]
    half2 = halves[1]
    i,j = 0,0
    while i < len(half1) and j < len(half2):
        if half1[i] <= half2[j]:
            mergedNums.append(half1[i])
            i += 1
        else:
            mergedNums.append(half2[j])
            j += 1
    print 'Merged: ',mergedNums

def bubbleSort(nums):
    pivot = 0
    for x in range(len(nums)):
        i = 0
        j = 1
        while j < len(nums):
            if nums[i] <= nums[j]:
                i += 1
                j += 1
            else:
                pivot = nums[i]
                nums[i] = nums[j]
                nums[j] = pivot
                i += 1
                j += 1
    print 'Bubble: ',nums

    

if __name__ == '__main__':
    mergeCombine(mergeConquer(mergeSplit(genNums(0,100))))
    bubbleSort(genNums(0,100))