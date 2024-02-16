# https://edabit.com/challenge/pihNcNQXiYHSRW8Cv

lst = ["may", "april", "september", "august"]


def sort_by_length(lst):
    lst = sorted(lst, key=len)
    return lst
print(sort_by_length(lst))