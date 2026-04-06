class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets=0
        cars=[]
        for i in range(len(position)):
            cars.append((position[i],speed[i]))
        cars=sorted(cars)
        time_to_reach=0
        for i in range(len(cars) - 1, -1, -1):
            time = (target - cars[i][0]) / cars[i][1]
            if time>time_to_reach:
                time_to_reach=time 
                fleets+=1
        return fleets