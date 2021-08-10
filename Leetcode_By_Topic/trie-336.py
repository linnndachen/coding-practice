class TrieNode:
    def __init__(self):
        self.next = collections.defaultdict(TrieNode)
        self.ending_word = -1
        self.palindrome_suffixes = []


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        trie = TrieNode()
        # insert words in reverse
        for i, word in enumerate(words):
            word = word[::-1]
            cur_level = trie

            # mark if the remainder is a palindrome
            for j, c in enumerate(word):
                if word[j:] == word[j:][::-1]:
                    cur_level.palindrome_suffixes.append(i)

                cur_level = cur_level.next[c]
            cur_level.ending_word = i


        solutions = []
        for i, word in enumerate(words):
            cur_level = trie

            for j, c in enumerate(word):
                # case 3: CAT SOLOS - TAC
                # found that there's a word matches
                if cur_level.ending_word != -1:
                    # and remainder is a palindrome
                    if word[j:] == word[j:][::-1]:
                        solutions.append([i, cur_level.ending_word])

                if c not in cur_level.next:
                    break
                cur_level = cur_level.next[c]

            else:
                # case 1: CAT - TAC
                # if we found the reversed version, insert the pair
                if cur_level.ending_word != -1 \
                    and cur_level.ending_word != i:
                    solutions.append([i, cur_level.ending_word])

                # case 2: CAT - SOLOS TAC
                # already found TAC/CAT and what's left is only palindrome
                for j in cur_level.palindrome_suffixes:
                    solutions.append([i, j])

        return solutions