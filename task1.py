#  https://edabit.com/challenge/xW6X8cQSHrcjpTXsn

s = "scoop"
def first_and_last(s):
    first = ''.join(sorted(s))
    last = ''.join(sorted(s)[::-1])
    a = [first,last]
    return a
print(first_and_last(s))