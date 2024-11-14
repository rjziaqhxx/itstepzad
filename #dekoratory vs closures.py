#dekoratory vs closures
def moj_dekorator(funkcje):
    def opakowanie():
        print('przed')
        funkcje()
        print('po')
    return opakowanie

@moj_dekorator
def p_func():
    print('w srod')

p_func()

def licznik():
    liczba = 0
    def zlicz():
        nonlocal liczba 
        liczba += 1
        return liczba
    return zlicz

counter = licznik()