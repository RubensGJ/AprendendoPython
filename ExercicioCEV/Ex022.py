nome = str(input('Qual é seu nome?'))
print('Seu nome em maiusculo é {}' .format(nome.upper()))
print('Seu nome em minusculo é {}' .format(nome.lower()))
print('Seu nome tem ao todso {} letras' .format(len(nome) - nome.count(' ')))
print('Seu primeiro tem {} letras' .format(nome.find(' ')))