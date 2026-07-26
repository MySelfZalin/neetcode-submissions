class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_fleets = []
        cars_stats = sorted(zip(position, speed), reverse=True)

        for pos,sp in cars_stats:
            if not car_fleets:
                time_to_finish = (target-pos)/sp
                car_fleets.append(time_to_finish)
                continue

            time_to_finish = (target-pos)/sp
            
            if car_fleets[-1] < time_to_finish:
                car_fleets.append(time_to_finish)

        return len(car_fleets)        


        