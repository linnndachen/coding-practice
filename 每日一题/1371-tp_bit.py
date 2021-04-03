class Solution:
    # "Time: O(n), Space: O(number of unique vowel count sequences)"
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}

        # seen: {010101 (a num that represent a combination of binary): last seen idx}
        seen, bit_count, result = {0: -1}, 0, 0

        for idx, char in enumerate(s):
            if char in vowels:
                # XOR, n would be 0 if count is even
                bit_count ^= vowels[char]

            # any combination of vowels that gives odd count & have not been seen before"
            if bit_count not in seen:  
                # "stores the oldest index for which a particular 
                # combination of vowels resulted into odd count"
                seen[bit_count] = idx
            else:
                # "if a combination is seen again, 
                # result = current_index - last_seen_index_for_this_combination"
                # "example: s = "aepqraeae" (odd vowel count for s[:2] 
                # is seen again at s[0:]"
                # "not considering character at last seen index will make count even"
                result = max(result, idx - seen[bit_count])

        return result