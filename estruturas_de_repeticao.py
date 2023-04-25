# FOR

texto = "GABRIEL"
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:     # upper = converte a letra de minúscula para maiúscula
        print(letra, end="")
else:
    print()

# FOR - RANGE

for numero in range(0,51,5):    # range(start, stop, step)
    print(numero, end="  ")

# WHILE

opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo extrato...")
else:
    print("Obrigado por usar nosso sistema bancário, até logo!")

