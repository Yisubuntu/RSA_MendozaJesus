# Práctica de algoritmo RSA
# Cifrado de mensaje

# 2024-02-14 - Anáhuac Mayab
import Crypto.Util.number as n
import Crypto as c

# Número de bits
bits = 1024

# Obtener los primos para Alice y Bob
pA = n.getPrime(bits, randfunc=c.Random.get_random_bytes)
print("pA: ",pA,"\n")
qA = n.getPrime(bits, randfunc=c.Random.get_random_bytes)
print("qA: ",qA,"\n")

pB = n.getPrime(bits, randfunc=c.Random.get_random_bytes)
print("pB: ",pB,"\n")
qB = n.getPrime(bits, randfunc=c.Random.get_random_bytes)
print("qB: ",qB,"\n")

# Obtenemos la primera parte de la llave pública de Alice y Bob
nA = pA * qA
print("nA: ",nA,"\n")

nB = pB * qB
print("nB: ",nB,"\n")

# Calculamos el Indicador de Euler Phi
phiA = (pA-1)*(qA-1)
print("phiA: ",phiA,"\n")

phiB = (pB-1)*(qB-1)
print("phiB: ",phiB,"\n")

# Por razones de eficiencia utilizaremos el número 4 de Fermat, 65537, debido a que es
# un primo largo y no es potencia de 2, y como forma parte de la clave pública 
# no  es necesario calcularlo

e = 65537

# Calcular la llave privada de Alice y Bob
dA = n.inverse(e, phiA)
print("dA: ",dA,"\n")

dB = n.inverse(e, phiB)
print("dB: ",dB,"\n")

# Ciframos el mensaje
msg = "Hola mundo"
print("Mensaje original: ",msg,"\n")
print("Longitud del mensaje en bytes: ",len(msg.encode("utf-8")),"\n")

# Convertir el mensaje a número
m = int.from_bytes(msg.encode("utf-8"), byteorder="big")
print("Mensaje convertido en entero: ",m,"\n")

# Ciframos el mensaje
c = pow(m, e, nB)
print("Mensaje cifrado: ",c,"\n")

# Desciframos el mensaje
des = pow(c, dB, nB)
print("Mensaje descifrado: ",des,"\n")

# Convertimos el mensaje de número a texto
msg_final = int.to_bytes(des, len(msg), byteorder="big").decode("utf-8")
print("Mensaje final: ",msg_final,"\n")