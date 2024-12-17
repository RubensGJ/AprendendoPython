import math

ang2= float(input('Qual é o seu angulo? '))
ang = math.radians(ang2)
print('O Cosseno de {} é de {:.2f}' .format(ang2, math.cos(ang)))
print('O Seno de {} é de {:.2f}' .format(ang2, math.sin(ang)))
print('O Tangente de {} é de {:.2f}' .format(ang2, math.tan(ang)))