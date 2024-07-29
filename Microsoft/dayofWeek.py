# https://algo.monster/problems/day_of_week

def solution(day, k):
    res = 0
    # calendar = {
    #     1 : 'Monday',
    #     2 : 'Tuesday',
    #     3 : 'Wednesday',
    #     4 : 'Thursday',
    #     5 : 'Friday',
    #     6 : 'Saturday',
    #     7 : 'Sunday''
    # }
    calendar = {
        'Monday': 1,
        'Tuesday': 2,
        'Wednesday': 3,
        'Thursday': 4,
        'Friday': 5,
        'Saturday': 6,
        'Sunday': 7
    }

    curr = calendar[day] + k % 7
    new = ''
    if curr > 7:
        present = curr - 7
        new = next(key for key, value in calendar.items() if value == present)
    else:
        new = next(key for key, value in calendar.items() if value == curr)
    return new
        

print('Monday || res =', solution('Monday', 3)) # res = Thursday
print('Tuesday || res =', solution('Tuesday', 101)) # res = Friday




