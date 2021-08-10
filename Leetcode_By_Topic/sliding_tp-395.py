class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        count = 0
        for i in range(1, 27):
            count = max(count, self.helper(s, k, i))
        return count
    
    def helper(self, s, k, max_char):
        """
        modified sliding window / two pointer, with dict keeping track of 
        number of uniq chars in the sliding window, and their counts 
        we calculate total number of distinct chars (max 26) first. 

        Loop from 1 to total_distinct_chars, get maximum substring length for 
        each distinct chars count, and return the max as result
        """
        start, end, count = 0, 0, 0
        unique_nums, more_than_k = 0, 0
        char = [0] * 128

        while end < len(s):
            # new char
            if char[ord(s[end])] == 0:
                unique_nums += 1
            char[ord(s[end])] += 1
            
            # satisfied condition
            if char[ord(s[end])] == k:
                more_than_k += 1
            end += 1

            # shrink the window
            while unique_nums > max_char:
                if char[ord(s[start])] == k:
                    more_than_k -= 1
                char[ord(s[start])] -= 1

                if char[ord(s[start])] == 0:
                    unique_nums -= 1
                start += 1

            if unique_nums == more_than_k:
                count = max(count, end - start)

        return count