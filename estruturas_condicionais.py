# IF

MAIOR_IDADE = 18
IDADE_ESPECIAL = 12

idade = int(input("Informe a sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade pode tirar a CNH")
elif idade == IDADE_ESPECIAL: # elif = else if
    print("Pode fazer a prova teórica, mas não as praticas")
else:
    print("Ainda não pode tirar a CNH")


# IF ANINHADO

conta_normal = False
conta_universitaria = True

saldo = 2000
saque = 2500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
    else:
        print("Não foi possível realizar o saque, saldo insuficiente!")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")
else:
    print("Sistema não reconheceu tipo de conta, entre em contato com o seu gerente")


# IF TERNÁRIO

saldo = 22000
saque = 2500

status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque!")