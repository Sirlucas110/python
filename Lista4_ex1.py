codEstado= int(input("Digite o cód do Estado de 1 a 5: "))
pesoTon= int(input("Digite o peso da carga em ton: "))
codCarga= int(input("Digite o cód da carga de 10 a 40: "))
pesoKg= pesoTon * 1000
imposto= 0
print("O peso em kg é ", pesoKg)
if codEstado <=1:
  imposto= pesoKg * 35/100
elif codEstado <= 2:
  imposto= pesoKg * 25/100
elif codEstado <= 3:
  imposto= pesoKg * 15/100
elif codEstado <= 4:
  imposto= pesoKg * 5/100
elif codEstado <= 5:
   pesoKg
print("O imposto é ",imposto)
preçoCarga= 0

if codCarga <= 20 and codCarga >=10:
    preçoCarga= pesoKg * 100
elif codCarga <= 30 and codCarga >=21:
    preçoCarga= pesoKg * 250
elif codCarga <= 40 and codCarga >= 31:
    preçoCarga= pesoKg * 340
print("O preço da carga é ",preçoCarga, "reais")

print("O valor total transportado é ", preçoCarga + imposto)
    


 



     