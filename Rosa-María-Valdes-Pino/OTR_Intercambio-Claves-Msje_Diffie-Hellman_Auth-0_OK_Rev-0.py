from datetime import datetime
from math import ceil, floor

print('Intercambio Autenticado de Claves por canal inseguro')
print('Método de Diffie-Hellman - OTR')
print('Codificado por Rosa Ma. Valdespino')
print('Para usarse a través de sistema de mensajería \n\n')

# Estos datos
P = 104623 # es para Hashy
P3 = 10001483086651246409081018999851691334875359091899
# opcion p = 2**521 - 1
G3 = 5952283703
pb1, pb2 = 104723, 104711


# Definición de Funciones funcionales.
# Función Hash de mientras
def Hashy(x,P3):
    h = ((x + x + ceil(P3/2))**3)%P3
    return h
# Fin función Hashy

# Inversa Modular
def Inv(a, b):
    if b < 0:
        b = b % a
    if a < b: # si se introducen al revés (menor primero) se voltean.
        c = a
        a = b
        b = c
    if b == 0:
        d = a

    A = a
    x2, x1, y2, y1 = 1, 0, 0, 1
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
        ye = y % A
        return ye
    else :
        return -1
    
# Generador de Aleatorios
def alea():
    ahorita = datetime.now()
    a = ahorita.microsecond     # Segundos instante actual
    b = ahorita.second          # micro-segundos entera de a
    k = (a * b)%P3              # parte fraccionaria de a
    if k < 100:
        k = k + 131415

    # Blum Blum Shub
    #print("k = ",k)
    c = int((k - floor(k))*1000)
    i = pow(2,c,(pb1 - 1)*(pb2 - 1))
    k = (pow(k,i,pb1*pb2))
    return k
# Fin Grador Aleatorios

def Enkr(m, SS):
    M = (m * SS)%P3
    return M

def Dekr(M, SS):
    SS1 = Inv(SS, P3)
    mm = (M * SS1)%P3
    return mm
      
# Inicia programa______---------------------------------__________

nada = 's'  # Es parte del repetidor del algoritmo
while nada == 's': # repetidor...
    entr1, entr2, entr3 = 0, 0, 0

    Ak = alea() # Llave para firmar (Secreta)
    
    # Diffie-Hellman, los hombres del infierno
    x = alea()
    ka = pow(G3,x,P3)
    # firmamos el ka
    aa = repr(ka)
    la = len(aa)
    fir = ka*10**la + Ak
    SignAk = Hashy(fir,P3)

    # Enviamos Ka y SignAk a B
    print("Envía lo siguiente a tu Comparsa sólo los números separados Ej 58781357987<=>835987589147 \n\n")
    print("   >>===========>>>        ka, SighnAk = ",ka ,"<=>", SignAk, "   <<<======<<")

    # Entramos kb y SignBk de Boberto
    
    while True:
        try:
            entr1 = entr1 + 1
            kbSignBk = input('Dame valor kb ySignAk de tu Comparsa Copia tal como llegó ').split('<=>') # Select Entrada datos
            kb = int(kbSignBk[0])
            SignBk = int(kbSignBk[1])
            break
        except ValueError:
            print("Dato mal, trata otra vez hasta que le des, al 4 truena")
            if entr1 >= 4:
                nada = 'n'
                print("-A- Demaisados errores, programa truena")
                break

    SS = pow(kb, x, P3) # Secreto Compartido

    # Entrada del Mensaje a encriptar
    while True:
        try:
            entr1 = entr2 + 1
            m = int(input('Dame el mensaje en número = ')) # Mensaje numerado
            break
        except ValueError:
            if entr2 <=1 :
                nada = 'n'
                print(' ') # Number, please, not alphanumeric
            else:
                
                break

    M = Enkr(m, SS)
    EK = Hashy(SS, P3)
    MK = Hashy(EK, P3)
    
    eMe = repr(M)
    ekk = len(eMe)
    eMMe = M*10**ekk + MK
    MAC = Hashy(eMMe, P3)
    print("Enviar a tu Comparsa lo siguiente: \n\n")
    print("   >>=========>>> Mensaje encriptado y MAC = ", M,"<=>",MAC, "  <<<=======<<")

    #_________----------------________________
    # Recepción del Mensaje del Comparsa
    # MAC(M, MK)
    # Boberto ha recibido ka, SignAk
    # Luego recibió M, MAC
    print("\n\n\n Recepción de Mensaje Comparsa")
    while True:
        try:
            entr3 = entr3 + 1
            eMeMAC = input('Dame el mensaje en número y MAC, separa2 por <=> = ').split('<=>') # Select prime,
            eMe = int(eMeMAC[0])
            MAC1 = int(eMeMAC[1])
            break
        except ValueError:
            if entr3 <=1 :
                print('Formato Solicitado, por Favor') # Number, please, not alphanumeric
            else:
                if entr3 >= 4:
                    nada = '1'
                    print('Demasiados intentos, fin del programa ') # <Spanish Joke for repeated error y pe = 1>
                    break

    if nada != 's':
        break

    eMe = int(eMeMAC[0])
    MAC1 = int(eMeMAC[1])
    
    emMee = len(repr(eMe))
    Mac = M*10**emMee + MK
    MAC1 = Hashy(Mac, P3)
    if MAC1 == MAC: # Si coinciden los MACs:
        mm = Dekr(eMe, SS)
        print("El mensaje que te enviaron = ", mm)
    else:
        print("Error de Autenticación, Mensaje fué Alterado en el camino ")
    
    #END Recepción Mensaje
    #---------________________------------------
    
    # Repetimitos o salimitos, el cierre del repetidor.
    nada =input('\n\nSólo ENTER para repetir ')
    if nada == '':
        print("Final del Programa \n\n")
        nada = 's'
        print("-S- Salimitos ", nada)
    else:
        nada = 'N'
    # Borramos las variables usadas para evitar lectura de memoria
    Ak, x, aa, Ak, fir, M, MAC = 0, 0, 0, 0, 0, 0, 0
    M, m, EK, MK, ekk, eMe, eMMe, Mac, MAC1 = 0,0,0,0,0,0,0,0,0
    print("Memoria Borrada ")
    # END IF
