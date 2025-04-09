# Bhaskara II fórmula ecuación Cuadrática

def Bhaskara(a, b, c):
    discrimi = b ** 2  -  4 * a * c
    print("-A- discriminante = ", discrimi)
    if abs(discrimi) < 0.000000000000004 :
        discrimi = 0
    if discrimi >= 0:
        print("-B-")
        x1 = ((-b) + discrimi ** 0.5 ) / (2 * a)
        x2 = ((-b) - discrimi ** 0.5 ) / (2 * a)
        return x1, x2
    else :
        print("-C-")
        j = complex(0,1)
        x1a = (-b)/(2 * a)  +  j*(abs(discrimi))**0.5 / (2 * a)
        x1b = (-b)/(2 * a)  -  j*(abs(discrimi))**0.5 / (2 * a)
        return x1a, x1b

banderlog = True
while banderlog == True :
    print("Ingresa coeficientes ecuación de 2° grado ")
    print("de la forma a*x^2 + b*x + c ")

    a = float(input("Ingresa valor de a "))
    b = float(input("Ingresa valor de b "))
    c = float(input("Ingresa valor de c "))

    x1, x2 = Bhaskara(a, b, c)
    if x1.imag > 0 :
        print("Valor de x1 = ", x1.real, "  +  ", x1.imag,"j ")
    else :
        print("Valor de x1 = ", x1.real, "  -  ", abs(x2.imag),"j ")

    if x2.imag > 0 :
        print("Valor de x2 = ", x2.real, "  +  ", x2.imag,"j ")
    else :
        print("Valor de x2 = ", x2.real, "  -  ", abs(x2.imag),"j ")

    selec = input("\nSi desea repetir sólo pulse ENTER the Matrix ")
    if selec == "" :
        banderlog = True
    else :
        banderlog = False
    # END while
    
