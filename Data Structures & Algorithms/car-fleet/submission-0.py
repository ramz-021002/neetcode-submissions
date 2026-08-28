class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = []
        for i in range(len(position)):
            time.append((target - position[i])/time[i])
        
        fleet = set(time)

        return len(fleet)
