idade = 1
soma = qntd = maioridade = qntdM = idadeMenorSalario = sexoMenorSalario = 0
menoridade = 1500
menorSalario = 10000000000000000000000000000000000000000001
media = 0

while idade > 0:
    idade = int(input('Digite a sua idade: '))
    if idade < 0: 
        break
    sexo = str(input('Digite seu sexo: {M,F}'))
    salario = float(input('Digite seu salário: '))
    if idade > 0:
        soma = soma + salario
        qntd = qntd + 1
        media = soma / qntd
        if idade < menoridade:
            menoridade = idade
        if idade > maioridade:
            maioridade = idade
        if sexo in 'Ff' and salario > 4000:
            qntdM = qntdM + 1
        if salario < menorSalario:
            menorSalario = salario
            idadeMenorSalario = idade
            sexoMenorSalario = sexo
    
   
print("A media salarial é ", media)
print("A pessoa mais nova tem ", menoridade)
print("A pessoa mais velha tem", maioridade)
print("A o numero de mulheres q tem salario maior que 4000 é ", qntdM)
print("O menor salario é ", menorSalario)
print("A idade da pessoa que tem o menor salario é ",idadeMenorSalario)
print("O sexo da pessoa com menor salario é: ", sexoMenorSalario)
