print('Funktory')

class Mnoznik:
    def __init__(self, mnoznik):
        self.mnoznik = mnoznik
    
    def __call__(self, x):
        return x * self.mnoznik
    
mnoz_przez_5 = Mnoznik(5)

wynik = mnoz_przez_5(10)

print(wynik)

#dekorator

def imie(imie):
    def moj_dekorator(funkcje):
        def opakowanie(*args, **kwargs):
            print(imie)
            print('przed')
            wynik = funkcje(*args, **kwargs)
            print('po')
            return wynik
        return opakowanie
    return moj_dekorator

@imie("dsa")
def p_func(a, b):
    print('w srod')
    return a+b

wynik = p_func(1,2)

#dekorator jako funkcja

class licznikwywolan:
    def __init__(self, funkcja):
        self.funkcja = funkcja
        self.licznik = 0
    
    def __call__(self, *args, **kwargs):
        self.licznik += 1
        print(f'wowylano {self.licznik} razy')
        return self.funkcja(*args, **kwargs)
    
@licznikwywolan
def p_func():
    print('dzialanie')

p_func()
p_func()



