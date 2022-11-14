
media = 0
contador = 1
soma = 0
for contador in range(1,151):
    n1 = int(input("Digite sua nota1: "))
    n2 = int(input("Digite sua nota2: "))
    soma = (n1*2+n2*3)
    media = soma / 5
    if media >= 7:
        print("aprovado")
        print(media)
    elif media < 5:
        print("reprovado")
        print(media)
    elif media >= 5 and media < 7:
        print("exame")
        print(media)
