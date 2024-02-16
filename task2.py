#  https://edabit.com/challenge/GaXXfmpM72yCHag9T

def unique(numbers):
    for num in numbers:
        if numbers.count(num) == 1:
            return num

print(unique(numbers = [4, 1, 1, 1, 1, 1, 1, 1]))