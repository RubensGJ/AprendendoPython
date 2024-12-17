import math

co = float(input('Comprimento cateto oposto'))
ca = float(input('Comprimento do cateto adjacente'))
hipo = (ca ** 2 + co ** 2) ** (1/2)
print('A hipotenusa é de {}'.format(hipo))