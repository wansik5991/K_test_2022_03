import os
os.system('cls')

import math
from collections import defaultdict
def getTime(in_time, out_time) :
    in_time = in_time.split(":")
    out_time = out_time.split(":")
    in_hour, in_min = int(in_time[0]), int(in_time[1])
    out_hour, out_min = int(out_time[0]), int(out_time[1])
    

    if out_min < in_min :
        out_min += 60
        out_hour -= 1
    total = (out_hour - in_hour) * 60 + (out_min - in_min)
    return total

def solution(fees, records):

    car = dict()
    parking_time = dict()
    cost = dict()

    for record in records :
        time, number, status = record.split()
        if status == 'IN' :
            car[number] = time
            parking_time.setdefault(number, 0)
        else :
            parking_time[number] += getTime(car[number], time)
            del car[number]

    if car :
        for car_left in car :
            parking_time[car_left] += getTime(car[car_left], '23:59')
    
    for number in parking_time :
        total_time = parking_time[number]
        total_price = int(fees[1])
        if total_time >= int(fees[0]) :
                total_time -= int(fees[0])
                total_price += math.ceil(total_time / int(fees[2])) * int(fees[3])
        cost[number] = total_price

    answer = []
    for result in sorted(cost.items()) :
        answer.append(result[1])
    return answer

print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
print(solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"] ))
print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))