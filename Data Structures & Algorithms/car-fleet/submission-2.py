class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_fleets = []
        cars_stats = sorted(zip(position, speed), reverse=True)

        for pos, sp in cars_stats:
            time_to_finish = (target-pos)/sp
            
            if not car_fleets or car_fleets[-1] < time_to_finish:
                car_fleets.append(time_to_finish)

        return len(car_fleets)        