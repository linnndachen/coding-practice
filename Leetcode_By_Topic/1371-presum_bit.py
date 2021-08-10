class Solution:
    """
    def findTheLongestSubstring(self, s: str) -> int:
        # freq[i:j] = freq[1:j] - freq[1:i-1]
        # if we want freq[i:j] to be even, then freq[1:j] and freq[1:i-1]
        # needs to be both even or both odd
        # because we are not looking for 1 target value, but the status of 
        # 5 letters, we use state compression to represent multiple status quo
        # thus, we need to freq[1:j], freq[1:i-1] to be 2 identical expression

        freq = {}
        freq[0] = -1
        count = [0, 0, 0, 0, 0]
        res = 0
        for j, char in enumerate(s):
            if char == "a":
                count[0] += 1
            elif char == "e":
                count[1] += 1
            elif char == "i":
                count[2] += 1
            elif char == "o":
                count[3] += 1
            elif char == "u":
                count[4] += 1

            key = self._count2key(count)

            if key in freq:
                res = max(res, j - freq[key])

            else:
                # we don't update an existing key
                # because we want the earliest index
                freq[key] = j

        return res
    
    def _count2key(self, arr):
        
        key = 0
        for i, n in enumerate(arr):
            # if it was odd count
            if n % 2 == 1:
                key += (1 << i)
        return key
    """

    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
        # d: last_seen_index_for_vowel_sequence_count_map
        d, count, result = {0: -1}, 0, 0
        
        for idx, char in enumerate(s):
            if char in vowels:
                # count would be 0 if count is even
                count ^= vowels[char]

            if count not in d:  
                d[count] = idx
            else:
                result = max(result, idx - d[count])

        return result