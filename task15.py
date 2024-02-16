# https://edabit.com/challenge/wPMgjmQMoCwm3G6mt

dates = ["Sept 22", "Sept 21", "Oct 15"]
month = input("Month: ")
def upload_count(dates,month):
    l = len(month)
    res = 0
    for i in dates:
        if i[:l] == month:
            res += 1
    return res

print(upload_count(dates,month))
