# OPERADORES ARITMÉTICOS
produto_1 = 20
produto_2 = 10

print("-------------------")
print("Operadores Aritméticos")
print("-------------------")
print(produto_1 + produto_2)
print(produto_1 - produto_2)
print(produto_1 / produto_2)
print(produto_1 // produto_2)
print(produto_1 * produto_2)
print(produto_1 % produto_2) # Resto da divisão
print(produto_1 ** produto_2) # Exponenciação

x = (10 + 5) * 4
y = (10 / 2) + (25 * 2) - (2 ** 2)
print(x)
print(y)
print("___________________")


# OPERADORES DE COMPARAÇÃO
print("-------------------")
print("Operadores de Comparação")
print("-------------------")

saldo = 200
saque = 200

print(saldo == saque)
print(saldo != saque)
print(saldo > saque)
print(saldo >= saque)
print("___________________")


# OPERADORES DE ATRIBUIÇÃO
print("-------------------")
print("Operadores de Atribuição")
print("-------------------")

saldo = 500
print(saldo)
saldo += 200
print(saldo)
saldo -= 100
print(saldo)
saldo //= 2
print(saldo)
print("___________________")


# OPERADORES LÓGICOS
print("-------------------")
print("Operadores Lógicos")
print("-------------------")

saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp)
print("___________________")


# OPERADORES DE IDENTIDADE
print("-------------------")
print("Operadores de Identidade")
print("-------------------")

saldo = 1000
limite = 500

print(saldo is limite)
print(saldo is not limite)
print("___________________")


# OPERADORES DE ASSOCIAÇÃO
print("-------------------")
print("Operadores de Associação")
print("-------------------")

frutas = ["limão","uva"]
curso = "Curso de Python"

print("laranja" in frutas)
print("uva" in frutas)
print("limão" not in frutas)
print("Python" in curso)