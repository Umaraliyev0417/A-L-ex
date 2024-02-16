# https://edabit.com/challenge/a55ygB8Bwj9tx6Hym

string = "abCBAaAAAAa"
def steps_to_convert(string):
    res = 0
    for x in string:
        if x.isupper():
            res += 1
    return res
print(steps_to_convert(string))