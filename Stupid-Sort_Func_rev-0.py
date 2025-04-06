# REM Inventado por Hamid Sarbazi Azad (Univ Sharif, Irán) Stupid Sort
# REM y Dick Grune
def stupid_Sort(vector):
    pos = 1
    while pos < len(vector):
        if vector[pos] >= vector[pos - 1]:
            pos = pos + 1
        else:
            c = vector[pos] # Intercambiar vector[pos] y vector[pos - 1]
            vector[pos] = vector[pos - 1]
            vector[pos - 1] = c # END Intercambiar
            if pos > 1:
                pos = pos - 1
            # REM END if
        # REM END if
    return vector
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
    

#
#
