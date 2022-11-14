numero = 1
qntd = qntd26 = qntd51 = qntd76 = 0
while numero >= 1:
    numero = int(input('Digite o numero: '))
    if numero >= 1 and numero <= 25:
        qntd = qntd + 1
    if numero >= 26 and numero <=50:
        qntd26 = qntd26 + 1
    if numero >= 51 and numero <= 75:
        qntd51 = qntd51 + 1
    if numero >= 76 and numero <= 100:
        qntd76 = qntd76 + 1

print(qntd)
print(qntd26)
print(qntd51)
print(qntd76)
    
    