# Programita bajo GPL-v3
# REM Inventado por Hamid Sarbazi Azad (Univ Sharif, Irán) Stupid Sort
# REM y Dick Grune
# Ordena 2 listas en base a la primera y manteniendo correspondencia original
#   entre elementos de la primera y de la segunda lista.

def Stupid_Sort(vector, vactor): # REM Ordenamos vactor según Vector
    ib,ii,taille = 1, 2, len(vector)
    while ib < taille:
        if vector[ib - 1] <= vector[ib]:
            ib,ii = ii, ii + 1
        else:
            vector[ib - 1], vector[ib] = vector[ib], vector[ib-1]
            vactor[ib - 1], vactor[ib] = vactor[ib], vactor[ib - 1]
            ib = ib - 1
            if ib == 0:
                ib,ii = ii, ii + 1
    return vector, vactor
# REM END SBR Function

entr0, entr1, entr2 = 0, 0, 0


vector, vactor = [], []
while True: # Entrada longitud cadena
    try:
        entr0 = entr0 + 1
        n = int(input('Dame el número de elementos de las cadenas N = ')) # Longitud de las Cadenas
        break
    except ValueError:
        if entr0 <=1 :
            print('Número, por favor, no alfanumérico') # Number, please, not alphanumeric
        else:
            print('NO Manches mi Bomberita, dije un número. ') # <Spanish Joke for repeated error y pe = 1>
            break

# Entrada para validador
for i in range(n):
    entraDita = input("Elementos Cadena separa2 por esPacio = ")
    
    x, y = entraDita.split()
    vector.append(x)
    vactor.append(y)
    
# NEXT i

lista, tonta = Stupid_Sort(vector, vactor)
for i in range(n):
    print("lista = ", lista[i], "     Tonta = ", tonta[i])
# NEXT i





