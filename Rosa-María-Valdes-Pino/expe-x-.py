# función e^x con maña

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
    
