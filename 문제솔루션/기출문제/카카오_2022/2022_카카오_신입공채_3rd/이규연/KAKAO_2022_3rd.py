import math


def solution(fees, records):
    answer = []
    for total_time in divide_records(records):
        answer.append(calc_fee(fees, total_time[1][0]))
    return answer


def divide_records(records):
    records_dict = dict()
    for i in records:
        time, car_num, state = i.split(' ')
        if car_num in records_dict.keys():
            if records_dict[car_num][1]:
                records_dict[car_num][0] += calc_time(records_dict[car_num][1], time)
                records_dict[car_num][1] = ''
            else:
                records_dict[car_num][1] = time
        else:
            records_dict[car_num] = [0, time, '']
    for key, value in records_dict.items():
        if value[1]:
            value[0] += calc_time(value[1], '23:59')
            value[1] = ''
    return sorted(records_dict.items())


def calc_time(s, e):
    sh, sm = map(int, s.split(':'))
    eh, em = map(int, e.split(':'))
    return (eh * 60 + em) - (sh * 60 + sm)


def calc_fee(fees, time):
    basic_time, basic_fee = fees[:2]
    unit_time, unit_fee = fees[2:]
    if time <= basic_time:
        return basic_fee
    else:
        return basic_fee + math.ceil((time - basic_time) / unit_time) * unit_fee


fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN",
           "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(fees, records))
