dias = int(input('Quantos dias o carro está alugado?'))
km = int(input('Quantos KM o carro rodou?'))
valorKm = km * 0.15
valorDias = dias * 60
valorTotal = valorKm + valorDias
print('Você deve R${:.2f} para a concessionária!'.format(valorTotal))  
