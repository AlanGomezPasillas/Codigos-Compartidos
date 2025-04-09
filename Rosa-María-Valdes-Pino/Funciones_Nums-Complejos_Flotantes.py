# Funciones para Complejos y Flotantes, bajo GPL v3

# ============================= #

# Conjugado de Complejo
def conju(z):
    j = (-1)**0.5
    conj = z.real - j*z.imag
    return conj

# Ángulo del Número Complejo
def arc(z):
    from math import atan, pi
    if abs(z.real) < 1e-10 :
        signy = z.imag/abs(z.imag)
        arc = 90*signy
        return round(arc, 9)
    elif abs(z.imag) < 1e-10 :
        signx = z.real/abs(z.real)
        if signx == 1 :
            arc = 0
            return arc
        else :
            arc = 180
            return arc
    else :
        arc = atan(z.imag/z.real)*180/pi
        signx = z.real/abs(z.real)
        signy = z.imag/abs(z.imag)
        if signx < 0 and signy > 0 :
            arc = round(arc, 9) + 180
            return arc
        elif signx < 0 and signy < 0 :
            arc = round(arc, 9) -180
            return arc
        else :
            arc = round(arc, 9)
            return arc
    # END if

# ============================= #

# Logaritmo Base a de Número, Numeración en base 10

def Loga(x, a):
    # calcular la característica
    x1 = x
    i = 0
    while x1 > a :
        x1 = x1/a
        i = i + 1
        # END while
    carac = repr(i)
    
    # Calcular la Mantisa
    x1 = x1**10 #x1^10 porque los números están expresa2 en base 10
    mantis = ""
    for i in range(15): # Obtener 15 DeciBienes, digo DeciMales
        j = 0
        while x1 > a :
            x1 = x1/a
            j = j + 1
            # END while
        mantis = mantis + repr(j)
        x1 = x1**10
    # NEXT i
    log = float(carac + '.' + mantis)
    return log

 # Cargar para Cálculos Eléctricos
 form math import sin, cos, tan, atan, acos, asin, log, exp
 j = (-1)**0.5

# =================================== #

# Función Gamma; aproximación de Lanczos
def gamma(z): # Ingerido de Wiki
    epsilon = 0.0000001
    def withinepsilon(x):
        return abs(x - abs(x)) <= epsilon

    from cmath import sin,sqrt,pi,exp

    p = [ 676.5203681218851,   -1259.1392167224028,  771.32342877765313,
         -176.61502916214059,     12.507343278686905, -0.13857109526572012,
            9.9843695780195716e-6, 1.5056327351493116e-7]
    z = complex(z)

    # Reflection formula
    if z.real < 0.5:
        result = pi / (sin(pi*z) * gamma(1-z))
    else:
        z = z - 1
        x = 0.99999999999980993

        for (i, pval) in enumerate(p):
            x = x + pval/(z+i+1)

        t = z + len(p) - 0.5
        result = sqrt(2*pi) * t**(z+0.5) * exp(-t) * x

    if withinepsilon(result.imag):
        return result.real
    return result

while True:
    try:
        z = float(input('Dame valor gamma (n - 1)! = '))
        break
    except ValueError:
        print('NO MAMUT, dije un número, va de nuez ')

x = gamma(z)
print(x)

# Error para Gamma(6) 2.1316282072803006e-13

# ============================= #

# función e^x con maña. Bajo GPL  v-3
def expe(x):
    from math import floor, log, factorial
    n = floor(x/log(2))
    xx = x - n*log(2)
    w = 0.0
    for i in range(30):
        yy = xx**i/factorial(i)
        w = w + yy
    # NEXT i
    ex = 2**n*w
    return ex

entr0 = 0
while True:
    try:
        entr0 = entr0 + 1
        X = float(input('Dame Valor de X para e^x = ')) # Longitud del claro de la Catenaria
        break
    except ValueError:
        if entr3 <=1 :
            print('Número, por favor, no alfanumérico') # Number, please, not alphanumeric
        else:
            print('NO Chingues mi Bomberita, dije un número; Salimos ') # <Spanish Joke for repeated error y pe = 1>
            break
            
y = expe(X)
print("exp(", X,") = ", y)

# Software bajo GPL V-3
# REM Inventado por Hamid Sarbazi Azad (Univ Sharif, Irán) Stupid Sort
# REM y Dick Grune
# REM Ordena 2 vectores tomando vector como base (ordena como (x, y))
def stupid_Sort(vector, vactor):
    pos = 1
    while pos < len(vector):
        if vector[pos] >= vector[pos - 1]:
            pos = pos + 1
        else:
            c, d = vector[pos], vactor[pos] # Intercambiar vector[pos] y vector[pos - 1]
            vector[pos], vactor[pos] = vector[pos - 1], vactor[pos - 1]
            vector[pos - 1], vactor[pos - 1] = c, d # END Intercambiar
            if pos > 1:
                pos = pos - 1
            # REM END if
        # REM END if
    return vector, vactor
    # REM END while

voctor = ['e', 'c', 'd', 'b', 'g', 'h', 'a', 'f']
vactor = [5, 3, 4, 2, 1, 6]

print(vactor, voctor)

tonta = stupid_Sort(voctor)
mensa = stupid_Sort(vactor)

a = input("Dame la cadena a ordenar ")

victor = []
for i in range(len(a)):
    victor.append(a[i])
# NEXT i
print("cadena = ", victor)

babosa = stupid_Sort(victor)

for i in range(len(tonta)):
    print("tonta(", i, ") = ", tonta[i])
# REM NEXT i
print()
for i in range(len(mensa)):
        print("mensa(", i, ") = ", mensa[i])
# NEXT i
print()
for i in range(len(babosa)):
    print("babosa(", '{0:2d}'.format(i), ") = ", babosa[i])
# NEXT i
print()
    
# x = [7, 10, 12, 4, 5, 13, 7, 10, 8, 11]
# >>> y = [25, 28, 36, 17, 21, 48, 28, 32, 27, 38]
'''
Maext = [16 13 12 17 12 17
18 17 11 17 15 17
15 15 14 14 16 16
14 16 15 13 17 14
16 19 13 14 18 15
17 15 12 17 14 19
11 16 17 11 18 12
16 17 13 16 16 15
16 19 14 13 18 12
16 16 14 15 16 15
11 19 18 9 20 10
15 14 14 15 15 18

>> version
ans = 6.2.0
>> xprom = mean(Maext)
xprom =

   15.083   16.333   13.917   14.250   16.250   15.000

'''
# 
#
 
