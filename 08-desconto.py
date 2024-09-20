preço = float(input('Digite o preço original: R$ '))
desconto = float(input('Digite o desconto %: '))

preço_final = preço - (preço*desconto / 100)

print(f"Preço com  desconto: R$ {preço_final:.2F}")