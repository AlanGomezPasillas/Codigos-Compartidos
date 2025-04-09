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
        z -= 1
        x = 0.99999999999980993

        for (i, pval) in enumerate(p):
            x += pval/(z+i+1)

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
