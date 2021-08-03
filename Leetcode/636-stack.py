class Solution:    
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        stack = []
        for string in logs:
            s = string.split(":")
            cur_id, status, time, = int(s[0]), s[1], int(s[2])
            if status == "start":
                if stack: # interupted
                    res[stack[-1][0]] += (time - stack[-1][1])

                stack.append([cur_id, time]) # start new task
            else: # end
                prev_id, prev_time = stack.pop()
                res[cur_id] += (time - prev_time + 1)
                if stack: # update the new start == cut out the idle time
                    stack[-1][1] = time+1
        return res
