print("-------------------------------------------------------")
print("Bem vindo à sua calculadora de 2 números!")
print("")
print("Qual operação deseja fazer?")
print(" 1 - Adição")
print(" 2 - Subtração")
print(" 3 - Multiplicação")
print(" 4 - Divisão")

Numero = input("Insira o que deseja fazer: ")

if Numero == "1":
    primeira = float(input("Insira seu primeiro número: "))
    segunda = float(input("Insira seu segundo número: "))
    resultado = primeira + segunda
    print(f"Resultado: {resultado}")
elif Numero == "2":
    primeira = float(input("Insira seu primeiro número: "))
    segunda = float(input("Insira seu segundo número: "))
    resultado = primeira - segunda
    print(f"Resultado: {resultado}")
elif Numero == "3":
    primeira = float(input("Insira seu primeiro número: "))
    segunda = float(input("Insira seu segundo número: "))
    resultado = primeira * segunda
    print(f"Resultado: {resultado}")
elif Numero == "4":
    primeira = float(input("Insira seu primeiro número: "))
    segunda = float(input("Insira seu segundo número: "))
    if segunda != 0:
        resultado = primeira / segunda
        print(f"Resultado: {resultado}")
    else:
        print("Erro: Divisão por zero!")
else:
    print("Opção inválida!")
