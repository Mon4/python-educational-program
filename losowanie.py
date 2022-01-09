import random
# losowanie małe jest uzywane do mnożenia i dzielenia
def losowanie_zmiennych_male():
    x = random.randrange(1, 10)
    y = random.randrange(1, 10)
    z = random.randrange(1, 10)
    return x, y, z

def losowanie_zmiennych_duze():
    x = random.randrange(1, 100)
    y = random.randrange(1, 100)
    z = random.randrange(1, 100)
    return x, y, z