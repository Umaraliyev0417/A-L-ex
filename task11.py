# https://edabit.com/challenge/rj7E4k6vSNZ9KpT9c


lst = [3, 6, 12, 36]
def factor_chain(lst):
    lst1 = []
    for x in lst:
        if lst[-1] % x == 0:
            lst1.append(x)
    return len(lst) == len(lst1)

print(factor_chain(lst))
