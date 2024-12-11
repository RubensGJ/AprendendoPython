def conversor_moeda():
    print("Conversor de Moeda")
    valor = float(input("Digite o valor em sua moeda: "))
    taxa = float(input("Digite a taxa de conversão (1 unidade da sua moeda para a moeda desejada): "))
    
    valor_convertido = valor * taxa
    print(f"O valor convertido é: {valor_convertido:.2f} na moeda desejada.")

conversor_moeda()
