import collections, bisect
class Solution:
    """
    # Time - O(N+all word length)
    # Space - O(M)
    def numMatchingSubseq(self, s1: str, words: List[str]) -> int:
        word_dict = defaultdict(list)
        count = 0

        # 1. group the same first letter tgt
        for word in words:
            word_dict[word[0]].append(word)    

        # 2. go to the next char in word
        for char in s1:
            words_expecting_char = word_dict[char]
            word_dict[char] = []
            for word in words_expecting_char:
                if len(word) == 1:
                    # Finished subsequence! 
                    count += 1
                else:
                    word_dict[word[1]].append(word[1:])

        return count
    """

    # binary search
    # Space O N
    def numMatchingSubseq(self, s1: str, words: List[str]) -> int:
        def _check(word):
            prev_idx = - 1

            for char in word:
                if char not in memo:
                    return False

                index = bisect.bisect(memo[char], prev_idx)

                if index >= len(memo[char]):
                    return False

                prev_idx = memo[char][index]

            return True

        memo = collections.defaultdict(list)

        for i, char in enumerate(s1):
            memo[char].append(i)

        res = 0
        for word in words:
            res += _check(word)

        return res

"""
class Solution:
    def numMatchingSubseq(self, s1: str, words: List[str]) -> int:
        def isSubseq(word):
            # previous char index
            prev = -1
            for char in word:
                if char not in memo: 
                    return False

                index = bisect.bisect(memo[char], prev)
                # previous char index must be before the current char index
                if index >= len(memo[char]): 
                    return False

                prev = memo[char][index]
            return True

        memo = collections.defaultdict(list)
        for i, c in enumerate(s1):
            memo[c].append(i)

        return sum([1 for word in words if isSubseq(word)])
"""