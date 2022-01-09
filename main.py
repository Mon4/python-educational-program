from tkinter import*
from tkinter import messagebox, font
from tkinter.filedialog import askopenfilename
from dzialanie import licz_dzialanie
from tekstowe import licz_tekstowe

l_pytan = 0
tryb = 0
licznik_dobre = 0
rownania = 0
polecenia = 0
tab_pliczek = 0
licznik_zadane = 0
e_odp = 0
odp = 0
e_pytanie1 = 0
lb_pytanie1 = None


#wczytywanie danych z pliku txt dla trybu gry - dzialania
def plik():
    global tab_pliczek
    with open(tab_pliczek[0], 'r') as file:
        global rownania
        rownania = []
        while True:
            line = file.readline()
            rownania.append(line.strip('\n'))  # zapisanie do tablicy porozdzielanych elementów z pliku
            if not line:
                break
    return rownania


#wczytywanie z pliku dla trybu gry - zadania tekstowe/ pola
def plik2(tryb):
    global tab_pliczek
    with open(tab_pliczek[tryb-1], 'r') as file:
        global rownania
        global polecenia
        rownania = []
        polecenia = []
        while True:
            line = file.readline()
            rownania.append(line.strip('\n'))  # zapisanie do tablicy porozdzielanych elementów z pliku
            line2 = file.readline()
            polecenia.append(line2.strip('\n'))  # co drugi element jest poleceniem
            if not line:
                break
    return rownania, polecenia


# wyświetlanie GUI do podawania ścieżek plików txt
def gui_otworz():
    lb_otworz.pack(side=TOP)
    btn_otworz.pack(side=TOP)

def koniec():
    btn_koniec.pack(side=BOTTOM)


# czytanie dla danego trybu odpowiedniej funkcji
def zadanie():
    global e_pytanie1
    global lb_pytanie1
    global odp
    if tryb == 1:
        odp, pytanie = licz_dzialanie(rownania)
    else:
        odp, pytanie = licz_tekstowe(rownania, polecenia)

    # wyświetlenie polecenia i pytanie o odpowiedz

    if lb_pytanie1 == None:
        lb_pytanie1 = Label(tk, text=pytanie, font=12)
        lb_pytanie1.pack()
    else:
        lb_pytanie1['text'] = pytanie

    e_pytanie1.pack()
    btn_odpowiedz.pack()


def sprawdz_l_pytan():
    global l_pytan
    l_pytan = e_l_pytan.get()
    if l_pytan.isdigit() == False:  # zapisanie liczby pytań od użytkownika
        e_l_pytan.delete(0, END)
        messagebox.showerror("", "Wpisz liczbę!")
        return

    l_pytan = int(e_l_pytan.get())
    licz_l_pytan()


def licz_l_pytan():
    global l_pytan
    global rownania
    global licznik_zadane
    global e_odp
    global odp
    global e_pytanie1

    lb_l_pytan.pack_forget()
    e_l_pytan.pack_forget()
    e_l_pytan.delete(0, END)  # clean entry
    btn_l_pytan.pack_forget()
    zadanie()


def trybo_pytania():
    lb_tryb.pack_forget()
    btn_tryb1.pack_forget()
    btn_tryb2.pack_forget()
    btn_tryb3.pack_forget()

    lb_l_pytan.pack()
    e_l_pytan.pack()
    btn_l_pytan.pack()


#reakcja na udzieloną odpowiedz
def reakcja(odp, e_odp, l_pytan, licznik_zadane):
    global licznik_dobre
    if odp == e_odp:
        licznik_dobre += 1
        messagebox.showinfo("Poprawna odpowiedz!", f"Poprawna odpowiedz!\nTwoja liczba punktów to: {licznik_dobre}/{licznik_zadane}.\n Pozostało {l_pytan-licznik_zadane} pytań do końca rundy.")
    else:
        messagebox.showerror("Błędna odpowiedź!", f"Błędna odpowiedź!\nPoprawna odpowiedź to: {odp}\nTwoja liczba punktów to: {licznik_dobre}/{licznik_zadane}.\nPozostało {l_pytan-licznik_zadane} pytań do końca rundy.")
    e_pytanie1.pack_forget()
    e_pytanie1.delete(0, END)
    btn_odpowiedz.pack_forget()


# funkcja sprawdzające czy koniec zadawania pytań
def zadawanie_pytan():
    global l_pytan
    global licznik_zadane
    global licznik_dobre
    global odp
    global e_pytanie1
    global rownania
    global polecenia
    global lb_pytanie1

    # sprawdzenie poprawności wpisu odpowiedzi
    try:
        e_odp = int(e_pytanie1.get())   # przypisanie
    except:
        # e_odp.delete(0, END)
        messagebox.showerror("", "Wpisz liczbę.")

    licznik_zadane += 1
    reakcja(odp, e_odp, l_pytan, licznik_zadane)

    if licznik_zadane < l_pytan:
        zadanie()
    else:
        btn_jeszcze_raz.pack()  # możliwość zagrania ponownie po ukończeniu odpowiedzi na wybraną ilośc pytań
        licznik_zadane = 0
        licznik_dobre = 0
        lb_pytanie1.destroy()
        lb_pytanie1 = None


# wybranie trybu, zawołanie funkcji wczytującej dane z pliku, wywołanie funkcji pytania o liczbę zadań
def tryb1():
    global tryb
    trybo_pytania()

    tryb = 1
    plik()

def tryb2():
    global tryb
    trybo_pytania()

    tryb = 2
    plik2(tryb)

def tryb3():
    global tryb
    trybo_pytania()

    tryb = 3
    plik2(tryb)


# wybór trybu-buttony:działania, tekstowe, pola
def wybierz_tryb():
    btn_jeszcze_raz.pack_forget()
    lb_tryb.pack(side=TOP)
    btn_tryb1.pack(side=TOP)
    btn_tryb2.pack(side=TOP)
    btn_tryb3.pack(side=TOP)


# sprawdzenie czy zostały odpowiednio wybrane pliki txt
def main():
    global tab_pliczek
    tab_pliczek = ['', '', '']
    n = 0
    while tab_pliczek[0] == tab_pliczek[1] or tab_pliczek[1] == tab_pliczek[2] or tab_pliczek[0] == tab_pliczek[2] or tab_pliczek[0] == '' or tab_pliczek[1] == '' or tab_pliczek[2] == '':  # jezeli mniej sciezek
        tab_pliczek.clear()
        if n == 1:
            messagebox.showinfo("", "Wybrałeś błędne ścieżki. Wybierz jeszcze raz.")
        tab_pliczek.append(askopenfilename(parent=tk))  #jezeli jest mniej niz 3 to dopisujemy scieżke
        tab_pliczek.append(askopenfilename(parent=tk))
        tab_pliczek.append(askopenfilename(parent=tk))
        n = 1
    btn_otworz.pack_forget()  # znikanie otwierania
    lb_otworz.pack_forget()

    if len(tab_pliczek) == 3:
        wybierz_tryb()


# stworzenie ekranu GUI
tk = Tk()
tk.geometry("1000x200")
tk.title("MATEMATYCZNE ŚWIRY")
tk.configure(background='gray')


# definiowanie buttonów i labelów
lb_otworz = Label(tk, text="Wybierz 3 kolejne pliki input txt z treściami zadań.", font=15)
btn_otworz = Button(tk, text='Otwórz', bg="blue", fg="white", command=lambda: main())
btn_koniec = Button(tk, text='Wyjście', bg="red", command=lambda: quit(exit))  #command = lamda to co ma się zrobic po wcisnięciu klawisza

lb_tryb = Label(tk, text="Wybierz tryb.")
btn_tryb1 = Button(tk, text="Działania", command=lambda: tryb1())
btn_tryb2 = Button(tk, text="Zadania tekstowe", command=lambda: tryb2())
btn_tryb3 = Button(tk, text="Pola figur",command=lambda: tryb3())

lb_l_pytan = Label(tk, text="Wpisz liczbę pytań na które chcesz odpowiedzieć.", font=15)
e_l_pytan = Entry(tk, width=10)
btn_l_pytan = Button(tk, text="Zatwierdź", bg="light green", command=lambda: sprawdz_l_pytan())

btn_odpowiedz = Button(tk, text="Zatwierdź", bg="light green", command=lambda: zadawanie_pytan())
e_pytanie1 = Entry(tk, width=10)

btn_jeszcze_raz = Button(tk, text="Zagraj jeszcze raz", command=lambda: wybierz_tryb())


gui_otworz()
koniec()

mainloop()