# Funcion Logaritmo base a
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


# Logaritmo base a, en base 10  Entrada Datitos
x = float(input("Valor a sacar Logaritmo = "))
a = float(input("Base del Logaritmo = "))
print("-1- x = ", x, "  a = ", a)
Log = Loga(x, a)
print("-D- Log = ", Log, "Tipo Log = ", type(Log))
print("Logaritmo base ", a, "   = ", Log)
