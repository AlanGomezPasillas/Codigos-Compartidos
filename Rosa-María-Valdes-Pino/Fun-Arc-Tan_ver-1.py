# Función Arco Tangente ángulos correctos +/- 180°
def arctan(z):
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

print("Arco Tangente de Número Complejo")
zeta = complex(input("Dame el Complejo = "))
angul = arc(zeta)
print("ángulo = ", angul)
