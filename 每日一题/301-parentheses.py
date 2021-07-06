from typing import List
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        count, remove = 0, 0
        
        for char in s:
            if char == "(":
                count += 1
            elif char == ")":
                count -= 1
            
            if count < 0:
                remove += 1
                count += 1

        remove += count
        maxlen = len(s) - remove
        self.res = []

        def _dfs(s, idx, cur_s, cnt):
            # boundary
            if cnt < 0:
                return
            # bounary
            if len(cur_s) > maxlen:
                return
            # exist condition
            if idx == len(s):
                if cnt == 0 and len(cur_s) == maxlen:
                    self.res.append(cur_s)
                return

            # for char
            if s[idx] not in "()":
                _dfs(s, idx+1, cur_s+s[idx], cnt)

            else: # 2 possibilities - 去重技巧
                if (len(cur_s) == 0) or s[idx] != cur_s[-1]:
                    _dfs(s, idx+1, cur_s, cnt)

                # if s[idx] == cur_s[-1], then we must choose the current idx
                # if s[idx] != cur_s[-1], we can choose or not choose
                if s[idx] == "(":
                    cnt += 1
                elif s[idx] == ")":
                    cnt -= 1
                    
                _dfs(s, idx+1, cur_s+s[idx], cnt)

        _dfs(s, 0, "", 0)

        return self.res