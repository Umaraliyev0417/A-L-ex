# https://edabit.com/challenge/pxSX4ywwGLFwXDRGy

names = ["Adam", "Emmy", "Tanya", "Emmy"]
enemies = input("Name: ")
def remove_enemies(names, enemies):
    result = []
    for name in names:
        if name not in enemies:
            result.append(name)
    return result

print(remove_enemies(names,enemies))
