"""
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
"""

"""
Comment: If use TreeSet, it will be O(NlogN). Use HashSet for O(N)
"""

def slow(array):
    """
    this solution is O(NlogN)
    """
    array.sort() #LogN
    res = 1
    for n in array: #N
        if n == res:
            res += 1
    return res

def fast(array):
    """
    this solution is O(N)
    """
    hash_map = {}
    for i in range(len(array)):
        if array[i]>0:
            hash_map[array[i]] == 1

    j = 1
    if 1 not in hash_map:
        return 1

    while j:
        if j not in hash_map:
            return j
        j+=1