# https://edabit.com/challenge/93o6y6WKFpQKoDg4T
def sort_by_length(lst):
    lst = sorted(lst, key=len)
    return lst
print(sort_by_length(lst = ["Turing", "Einstein", "Jung"]))