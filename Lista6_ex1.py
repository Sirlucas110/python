inteiro = 1
soma = 0
qntd = 0
while inteiro > 0:
    inteiro = int(input('Digite o numero inteiro: '))
    if inteiro > 0:
        soma = soma + inteiro
        qntd = qntd + 1
        media = soma/qntd
print(soma)
print(media)
