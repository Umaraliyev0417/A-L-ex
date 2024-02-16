# https://edabit.com/challenge/PTh7tBusAZRgjAWEZ

obj = {"skate": 10, "painting": 20 }
limit = int(input("Son: "))
def calc_diff(obj, limit):
    result = 0
    for x in obj:
        result += obj[x]
    return (result - limit)

print(calc_diff(obj, limit))