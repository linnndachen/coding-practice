class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        end = len(arr) - 1
        
        while end > 0 and arr[end - 1] <= arr[end]:
            end -= 1
        
        start = 0
        res = end - start
        
        if res == 0:
            return 0
        
        # find the remove window
        while end <= len(arr):
            # as long as the starting point was 0 OR inorder 
            # and starting part's last inorder index <= ending part's first index
            # keep it
            while (start == 0 or arr[start - 1] <= arr[start]) \
                and (end == len(arr) or arr[start] <= arr[end]):
                start += 1
                res = min(res, end - start)
                
                if res == 0:
                    return 0
            end += 1
        return res