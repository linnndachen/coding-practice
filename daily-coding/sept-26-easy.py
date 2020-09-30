"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

def search(lst_of_numbers, k):
    found = False
    lst_of_numbers.sort()
    for i in lst_of_numbers:
        need = k-i
        l = 0
        r = len(lst_of_numbers)-1
        while (r-l) != 0:
            mid = (r-l)//2 + 1
            if lst_of_numbers[mid] == need:
                found = True
                break
            elif lst_of_numbers[mid] < need:
                l = mid+1
            elif lst_of_numbers[mid] > need:
                r = mid-1
    return found


print(search(lst_of_numbers=[10, 15, 3, 7], k=17))