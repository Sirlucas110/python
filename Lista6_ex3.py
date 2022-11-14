opção = 0
while opção != 3:
    print('1 - Media Aritmetica')
    print('2 - Media Ponderada')
    print('3 - Sair do programa')
    opção = int(input('Digite a opção: '))
    if opção == 1:
        n1 = int(input('Digite a nota1: '))
        n2 = int(input('Digite a nota2: '))
        media = (n1 + n2)/2
        print('A media é ', media)
    if opção == 2:
        n1 = int(input('Digite a nota1: '))
        n2 = int(input('Digite a nota2: '))
        n3 = int(input('Digite a nota3: '))
        p1 = int(input('Digite o peso1: '))
        p2 = int(input('Digite o peso2: '))
        p3 = int(input('Digite o peso3: '))
        media = (n1*p1 + n2*p2 + n3*p3)/(p1 + p2 + p3)
        print('A media ponderada é: ', media)
    if opção == 3:
        print('Saindo do Programa')
    if opção > 3 or opção < 0:
        print('Opção invalida')

print('Programa finalizado')


    