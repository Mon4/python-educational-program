from losowanie import losowanie_zmiennych_duze, losowanie_zmiennych_male
import random

def licz_dzialanie(rownania):
    dzialanie = random.choice(rownania)  # wylosowanie jednego dzialania z tablicy rownan
    while dzialanie == '':  # usuwanie pustej linijki na koncu
        dzialanie = random.choice(rownania)

    if dzialanie == 'x / y' or dzialanie == 'x * y':  # losowanie x, y, z w zależności od typu dzialania
        x, y, z = losowanie_zmiennych_male()
    else:
        x, y, z = losowanie_zmiennych_duze()

    odp = int(eval(dzialanie))  # obliczanie prawidlowej odpowiedzi

    if dzialanie == 'x / y':  # wyjatek - dzielenie liczb calkowitych
        temp = x * y
        y = x
        x = temp
        odp = int(x / y)

    dzialanie = dzialanie.replace(" ", "")  # usuwanie spacji z dzialania

    if len(dzialanie) == 3:  # zapiasanie polecenia do zmiennej
        pytanie = (str(x) + dzialanie[1] + str(y) + '=')
    elif len(dzialanie) == 5:
        pytanie = (str(x) + dzialanie[1] + str(y) + dzialanie[3] + str(z) + '=')

    return odp, pytanie

