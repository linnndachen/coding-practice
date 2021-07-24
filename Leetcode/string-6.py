class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # zigzag pattern the period is (numRows - 1)*2 (one up + one down)
        if numRows == 1: 
            return s
        rows = [''] * numRows
        num = (numRows-1)*2 # 6
        for i, item in enumerate(s):
            if i % num >= numRows:
                # 中间的斜着上去的数字
                rows[(num - i % num)] += item
            else:
                # 竖下来的数字
                rows[i % num] += item
        return ''.join(rows)