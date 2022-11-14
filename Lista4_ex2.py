codProduto= int(input("Digite o codigo de 1 a 40: "))
qtdComprada= int(input("Digite a quantidade comprada: "))
preço= 0
if codProduto <= 10 and codProduto >= 1:
  preço= qtdComprada * 10
elif codProduto <= 20 and codProduto >= 11:
  preço= qtdComprada * 15
elif codProduto <= 30 and codProduto >= 21:
  preço= qtdComprada * 20
elif codProduto <= 40 and codProduto >= 31:
  preço= qtdComprada * 30
print("O preço total é",preço)
preçoUnt= preço / qtdComprada
print("O preço unitario é", preçoUnt)

desconto= 0
if preço <= 250:
    desconto= preço * 5/100
elif preço <= 500:
    desconto= preço * 10/100
elif preço > 500:
    desconto= preço * 15/100
print("O preço com desconto é",preço - desconto)




   