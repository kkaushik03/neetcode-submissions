class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)  # closest to target first
        fleets = 0
        lead = 0.0
        for pos, spd in cars:
            time = (target - pos) / spd
            if time > lead:      # can't catch up -> new fleet
                fleets += 1
                lead = time
        return fleets