frase = '  Curso em video Python  '

# Imprime a string com espaços no início e no final.
print(frase)
# Exibe caracteres da string de índice 0 a 12 (exclusivo), pulando de 2 em 2.
print(frase[0:13:2])
# Conta quantas vezes o caractere 'o' aparece na string.
print(frase.count('o'))
# Converte todos os caracteres da string para maiúsculas.
print(frase.upper())
# Calcula o comprimento total da string, incluindo os espaços.
print(len(frase))
# Remove os espaços em branco do início e do final da string.
print(frase.strip())
# Substitui a palavra 'Python' por 'Rubens' na string.
print(frase.replace('Python', 'Rubens'))
# Verifica se a palavra 'Curso' está contida na string.
print('Curso' in frase)
# Retorna o índice onde a sequência 'em' aparece pela primeira vez.
print(frase.find('em'))
# Converte todos os caracteres da string para minúsculas.
print(frase.lower())
# Divide a string em uma lista de palavras, removendo espaços extras.
print(frase.split())
