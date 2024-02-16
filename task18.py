str = input("enter word: ")

def find_vowels(string):
    result = 0
    vowels = "aouie"
    for alp in string:
        if alp in vowels:
            result += 1

    print(result)


find_vowels(string=str)