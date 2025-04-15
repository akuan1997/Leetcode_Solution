class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        current_tank = 0
        total_tank = 0
        start_position = 0

        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]
            current_tank += gas[i] - cost[i]

            if current_tank < 0:
                start_position = i + 1
                current_tank = 0

        return start_position if total_tank >= 0 else -1