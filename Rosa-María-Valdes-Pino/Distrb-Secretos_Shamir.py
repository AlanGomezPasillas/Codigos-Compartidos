# Esquema de Shamir para distribuír secreto mensajes cortos
from time import clock
import sys

p = 10001483086651246409081018999851691334875359091899

def invMod(a, b):
    inver, Bander = 0, 0
    if a < b: # si se introducen al revés (menor primero) se voltean.
        c = a
        a = b
        b = c
        
    if b == 0:
        d = a
        print('un número es cero, d = ', a, 'x = 1 y y = 0')
        sys.exit(1)
    A = a
    B = b

    x2, x1, y2, y1 = 1, 0, 0, 1
    
    while b > 0:
        q = a // b
        r = a - q * b
        x = x2 - q * x1
        y = y2 - q * y1

        a = b
        b = r
        x2 = x1
        x1 = x
        y2 = y1
        y1 = y
        # print('q = ', q, 'r = ', r, 'x = ', x, 'y = ', y, 'y1 = ', y1)
	
    # REM fin del while, a > b
    d = a
    x = x2
    y = y2
    if d == 1:
        #print('inverso de ', B, ' módulo ', A,' es = ', y % A)
        inver = y % A
    else :
        print('Número no tiene Inversa ')
        sys.exit(2)
        Bander = 1
    return inver

def validate_user_input(entra_varios: str) -> bool:
    try:
        row, col = entra_varios.split()
    except ValueError:
        print("Mala entrada: >La entrada son exactamente 2 números separados por un EsPacio.")
        return False
    
    try:
        row = int(row)
        col = int(col)
    except ValueError:
        print("La entrada son 2 números, no diste número o diste alfanumérico.")
        return False
    if row < 0 :
        print("Primer número menor que cero")
        return False
    if col < 0 :
            print("Segundo número menor a cero.")
            return False
    # END ifs
    
    return True


def alea():
    x = [[0 for i in range(2)] for i in range(m)]
    ahorita = clock()
    a = ahorita
    b = int(a)          # parte entera de a
    c = a - b           # parte fraccionaria de a
    d = int(c * 1e48) # convertir fracc en otro entero.
    f = (b + d)%p
    if f < 10:
        f = f + 10
    return f
# Fin Grador Aleatorios

def GeneraShamir(k, m, S, p):
    a, x, y = [], [], [0 for i in range(m)]
    a.append(S)
    for i in range(1, k):
        a.append(alea())
    # NEXT i
    #print("-B1- Vector a = ", a)
    
    for i in range(m):
        x.append(alea())
    # NEXT i
    for i in range(m):
        for j in range(k):
            y[i] = (y[i] + a[j]*x[i]**j)%p
        # NEXT j
    # NEXT i
    return x, y

def RecuperaShamir(x, y, p):
    S = 0 
    for j in range(k):
        d = 1
        for m in range(k):
            if m != j:
                d = (d*(x[m]*invMod((x[m] - x[j])%p, p)))%p
        # NEXT m
        S = S + y[j]*d
    # NEXT j
    return int(S)%p

nada = 's' # Inicia el Repetidor
while nada == 's':
    algo = 's'
    while algo == 's':
        selec = input('Crear Secreto "C" ó Recuperar Secreto "R" ')
        print()
        if selec == 'c' or selec == 'C':
            selec = 'c'
            algo = 'n'
        # END if
        if selec == 'r' or selec == 'R':
            selec = 'r'
            algo = 'n'
        # END if
    
    if selec == 'c':
        # Valores de arranque lectura variables
        entr0, entr1, entr2 = 0, 0, 0
        # Entradita de Datitos
        while True:
            try:
                entr0 = entr0 + 1
                k = int(input('Dame número mínimo datos para reconstruír  k = '))
                print()
                break
            except ValueError:
                if entr0 <=1 :
                    print('Número, por favor, no alfanumérico')
                else:
                    print('NO MANCHES MI BOMBERITA, dije un número, va de nuez ')
                    break

        while True:
            try:
                entr1 = entr1 + 1
                m = int(input('Dame número de entidades para distriíbur m = '))
                print()
                if m > 15:
                    m = 15
                break
            except ValueError:
                if entr1 <=1 :
                    print('Número, por favor, no alfanumérico')
                else:
                    print('NO MANCHES MI BOMBERITA, dije un número, va de nuez ')
        
        while True:
            try:
                entr2 = entr2 + 1
                S = int(input('Dame el Secreto convertido a número = '))
                print()
                break
            except ValueError:
                if entr2 <=1 :
                    print('Número, por favor, no alfanumérico')
                else:
                    print('NO MANCHES MI BOMBERITA, dije un número, va de nuez ')

        x, y = GeneraShamir(k, m, S, p)
        for i in range(m):
            print("RESULTADO x(",i,") = ", x[i],"   y(",i,") = ", y[i])

    if selec == 'r':
        # Entra primero el valor de k
        entr0 = 0
        while True:
            try:
                entr0 = entr0 + 1
                k = int(input('Dame número mínimo datos para reconstruír  k = '))
                print()
                break
            except ValueError:
                if entr0 <=1 :
                    print('Número, por favor, no alfanumérico')
                else:
                    print('NO MANCHES MI BOMBERITA, dije un número, va de nuez ')
                    break
        #END while

        # Entran los pares de números
        x, y = [0 for i in range(k)], [0 for i in range(k)]
        for i in range(k):
            valid_input = False # Se considera entrada incorrecta hasta que se verifique.
            while not valid_input:
                entra_varios = input("Valores x y sepra2 esPacio = ")
                print()
                valid_input = validate_user_input(entra_varios)
        
            a, b = entra_varios.split()
            x[i], y[i] = int(a), int(b)
        # NEXT i

        S = RecuperaShamir(x, y, p)
        print("El Secreto es = ", S)
        print()

    # Selector Repetidor, si repetimos el programa
    print()
    algo = input('Repetir? Sólo pulse ENTER (The Matrix) ')
    if algo == '':
        nada = 's'
    else:
        nada = 'n'
    # END IF

