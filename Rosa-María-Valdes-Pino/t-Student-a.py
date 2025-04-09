from scipy import integrate
from scipy.special import gamma, factorial
from math import pi

print("Codificado por Pink Valdespino")
print("debes tener numpy-scipy instalado para que funcione")
print("integra t-Student de 0 al valor deseado ")


def Student(t,k):
    a = gamma((k + 1)/2)
    b = gamma(k/2)
    c = (1 + t**2/k)**(-(k + 1)/2)
    h = a*c/((pi*k)**0.5*b)
    return h



nada = 's'  # Es parte del repetidor del algoritmo
while nada == 's': # repetidor...
    entr1, entr2 = 0, 0


    while True:
        try:
            entr1 = entr1 + 1
            t = float(input('Dame el valor de Zt de T-Student = ')) # Select prime,
            break
        except ValueError:
            if entr1 <=1 :
                print('Número, por favor, no alfanumérico') # Number, please, not alphanumeric
            else:
                pe = 1
                print('NO Manches mi Bomberita, dije un número; será 1 ') # <Spanish Joke for repeated error y pe = 1

    
    while True:
        try:
            entr2 = entr2 + 1
            k = int(input('Dame los Graditos de libertad usados = ')) # Select prime,
            break
        except ValueError:
            if entr1 <=1 :
                print('Número, por favor, no alfanumérico') # Number, please, not alphanumeric
            else:
                pe = 1
                print('NO Manches mi Bomberita, dije un número; será 1 ') # <Spanish Joke for repeated error y pe = 1


    tst = integrate.quad(lambda x: Student(x,k), 0, t)
    coli = 0.5 - tst[0]
    print("\n \n")
    print("Valor probabilidad = ","{0:.5f}" .format(tst[0]))
    print("                        Valor colita = ","{0:.5f}".format( 0.5 - tst[0]))
    print("Error máximo InnTegración en ppm = ","{0:.4e}".format(coli))
                
    # Repetimitos o salimitos, el cierre del repetidor.
    nada =input('\n\nSólo ENTER para repetir ')
    if nada == '':
        print("Final del Programa \n\n")
        nada = 's'
        print("-S- Salimitos ", nada)
    else:
        nada = 'N'
