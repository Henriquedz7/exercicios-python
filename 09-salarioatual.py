salario_atual = float(input('Informe o salario atual: R$ '))
percentual_aumento = float(input('Informe p precentual de aumento: '))

novo_salario =salario_atual + (salario_atual * (percentual_aumento / 100))

print(f"O novo salario é: R$ {novo_salario:.2f}")