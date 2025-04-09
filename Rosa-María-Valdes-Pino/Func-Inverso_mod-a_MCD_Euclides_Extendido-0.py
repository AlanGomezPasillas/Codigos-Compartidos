# entrada: dos enteros positivos a, b con a <= b
# Salida: d = MCD y x, y tal que ax + by = d

print('dados a y b, obtendrás MCD y (x, y) tal que a*x + b*y = MCD')
print('si MCD = 1, dará inverso del menor módulo del mayor \n pueden darse en cualquier orden')
print('Dará inverso de a mod b si MaxComunDivisor es 1, \n de otra manera NO EXISTE INVERSO \n')

###______________________________________________###
def invMod(a, b):
    inver, Bander = 0, 0
    if a < b: # si se introducen al revés (menor primero) se voltean.
        c = a
        a = b
        b = c

    if b == 0:
        d = a
        print('un número es cero, d = ', a, 'x = 1 y y = 0')

    A = a
    B = b
    x2, x1, y2, y1 = 1, 0, 0, 1
    print('b = ', b)

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

    # REM fin del while, a > b
    d = a
    x = x2
    y = y2
    if d == 1:
        inver = y % A
    else :
        Bander = 1
        
    return inver, Bander, d, x, A, y, B
# REM END Función

nada = 's'
Banderlog = 0
while nada == 's':
    entr1, entr2 = 0, 0
    while True:
            try:
                entr1 = entr1 + 1
                x = int(input('Dame valor mayor (a ò m) = '))
                break
            except ValueError:
                if entr1 <=1 :
                    print('Número, por favor, no alfanumérico')
                else:
                    print('NO MANCHES MI BOMBERITA, dije un número, va de nuez ')

    while True:
        try:
            entr2 = entr2 + 1
            y = int(input('Dame valor a obtener inverso  (b) = '))
            break
        except ValueError:
            if entr2 <=1 :
                print('Número, por favor, no alfanumérico')
            else:
                print('NO MANCHES MI BOMBERITA, dije un número, va de nuez ')    
    
    inversa, Banderlog, d, x, A, y, B = invMod(x, y)

    if Banderlog == 0:
        print('MaxCommDiv =   x  *   a   +   y  *   b')
        print('  MCD = ', d, ' = ', x, ' * ', A, ' + ', y, ' * ', B)
        print("inversa de ", B, " módulo ", A," es = ", inversa)
    else:
        print('No hay inverso de ', B, '(mod', A,')')
    # REM END if
    
    algo = input('Repetir? -Sólo Enter the Matrix para instroduzca caracter ')
    if algo == '':
        nada = 's'
    else:
        nada = 'no'
    # END IF
