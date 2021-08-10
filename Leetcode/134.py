from typing import List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # [1,2,3,4,5] = 15
        # [3,4,5,1,2] = 15
        n = len(gas)
        t_gas, cur_gas, start_station = 0, 0 , 0

        for i in range(n):
            t_gas += gas[i] - cost[i]
            cur_gas += gas[i] - cost[i]
            
            if cur_gas < 0:
                start_station = i + 1
                cur_gas = 0

        return start_station if t_gas >= 0 else -1