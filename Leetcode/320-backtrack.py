class Solution:
    def generateAbbreviations(self, word: str):

        def helper(curr_l, cur, count):
            """
            curr_l: current length of the current string
            cur: current string

            Return: a list of all the possible abbre words
            """
            if curr_l == len(word):
                res.append(cur + str(count) if count > 0 else cur)
            else:
                # abbre the next char
                helper(curr_l + 1, cur, count + 1)

                #keep the next char
                helper(curr_l + 1, cur + (str(count) if count > 0 else '') + word[curr_l], 0)


        res = []
        helper(0, '', 0)
        return res

test = Solution()
print(test.generateAbbreviations(word = "word"))