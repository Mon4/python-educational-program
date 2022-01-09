import random
from losowanie import losowanie_zmiennych_duze, losowanie_zmiennych_male

def licz_tekstowe(rownania, polecenia):
    dzialanie = random.choice(rownania)  # wylosowanie jednego dzialania z tablicy rownan
    while dzialanie == '':  # usuwanie pustej linijki na koncu
        dzialanie = random.choice(rownania)

    index = rownania.index(dzialanie)
    polecenia = polecenia[index]

    dzialanie = dzialanie.replace(" ", "")
    if dzialanie[1] == '*' or dzialanie[2] == '*' or dzialanie[1] == '/' or dzialanie[2] == '/':  # dla mnożenia i dzielenia losowanie małych liczb
        x, y, z = losowanie_zmiennych_male()
    else:
        x, y, z = losowanie_zmiennych_duze()

    if dzialanie == 'x/y':  # wyjatek - dzielenie liczb calkowitych
        temp = x * y
        y = x
        x = temp
        odp = int(x / y)

    odp = int(eval(dzialanie))
    x = str(x)
    y = str(y)
    z = str(z)
    polecenia = polecenia.replace("#x", x)  # zamiana z #x na wartosc wylosowaną x
    polecenia = polecenia.replace("#y", y)
    polecenia = polecenia.replace("#z", z)

    pytanie = polecenia
    return odp, pytanie
