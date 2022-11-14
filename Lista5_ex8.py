mediasala = 0 
maiormedia = 0
totalSete = 0
somasala = 0
menormedia = 10
qntd = 0
for contador in range(1,4):
    p1 = int(input("Digite a nota da p1: "))
    p2 = int(input("Digite a nota da p2: "))
    soma = 0
    media = 0
    soma = p1+p2
    qntd = qntd + 1
    media = soma / 2
    somasala = somasala + media
    mediasala = somasala / qntd
    if media > maiormedia:
        maiormedia = media
    if media < menormedia:
        menormedia = media
    if media >= 7:
        totalSete = totalSete + 1
    print('media', media)



print('somasala', somasala)
print('mediasala', mediasala)
print('menormedia', menormedia)        
print('maiormedia', maiormedia)
print(totalSete)

