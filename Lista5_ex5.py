total = 0
totalz = 0
for contador in range(1,11):
    n = int(input("Digite um numero: "))
    if n > 0:
        total = total + 1
    elif n == 0:
        totalz = totalz + 1
    

        
print("Tem ", total, "números positivos")
print("Tem", totalz, "zeros digitados")