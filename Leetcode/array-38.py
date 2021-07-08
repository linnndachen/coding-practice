class Solution:
    def countAndSay(self, n: int) -> str:
        res = "1"
        for _ in range(n-1):
            cnt = 1
            tmp = []

            for idx in range(1, len(res)):
                if res[idx] == res[idx-1]:
                    cnt += 1
                else:
                    tmp.append(str(cnt))
                    tmp.append(res[idx-1])
                    cnt = 1

            tmp.append(str(cnt))
            tmp.append(res[-1])
            res = "".join(tmp)

        return res