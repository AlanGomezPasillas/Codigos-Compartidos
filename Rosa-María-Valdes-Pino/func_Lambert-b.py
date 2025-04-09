# Programa bajo GPL v-3
# Función de Lambert por serie de Taylor
# Porgrama por Rosa María M: Valdespino bajo GPL v3

def Lambert(b) :
    from math import exp
    def NewtRaph(x, b) :
        x0 = x
        for n in range(1, 1000): # Máximo 1000 iteraciones; podría ser variable
            x1 = x0 - (x0*exp(x0) - b)/(exp(x0) + x0*exp(x0))
            xref = x0
            x0 = x1
        
            if abs(xref - x1) <= 0.0000000000005 :# Es la Tolerancia; Excesiva para ingeniería
                break  # Su se cumple xi - xi-1 < tol; se Rompé el bucle y sale
            # END if
        # NEXT n
        if n == 999 :
            print("Cálculo aproximado, iteraciones máximas excedidas")
        # END if
        x = x1
        return x
    # END Función
    if b >= 0 :

        y1, y2 = NewtRaph(0, b), "No hay W-1"
        return y1, y2
    else :
        y1, y2 = NewtRaph(0, b), NewtRaph(-2, b) # Si x será < 1/e
        return y1, y2
    # END if

print("Programa bajo GPL v-3 \n")

# Algoritmos para Validar entrada y repetir salida.
nada = 's'
while nada == 's': # Esta sección es para repetir el algoritmo hasta que se entre caracter.
    entr1 = 0

    while True:
            try:
                entr1 = entr1 + 1
                x = float(input('Ingresa Valor a calcular Función Lambert = '))
                break
            except ValueError:
                if entr1 <=1 :
                    print('Número, por favor, no alfanumérico')
                else:
                    print('NO MANCHES MI BOMBERITA, dije un número, va de nuez ')

    print()
    y1, y2 = Lambert(x)

    if isinstance(y2, str) == True :
        print(round(y1, 11), y2)
    else :
        print(round(y1, 11), round(y2, 11))

    # Este es la sección final de Repetición de Cálculos.
    # Para repetir pulsqar sólo Enter the Matrix.
    nada = input('Si quiere Repetir sólo Pulse Enter The Matrix ')
    if nada == '' :
        nada = 's'
    else :
        nada = 'n'
    # END if

