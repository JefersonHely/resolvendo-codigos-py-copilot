# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

# Receber dois dados do usuário
primeiro_dado = int(input("Digite o primeiro dado: "))
segundo_dado = int(input("Digite o segundo dado: "))

# Receber a operação desejada
operacao = input("Digite a operação desejada (+, -, *, /): ")

# Realizar a operação escolhida e calcular o resultado
if operacao == "+":
    resultado = abs(primeiro_dado + segundo_dado)
elif operacao == "-":
    resultado = abs(primeiro_dado - segundo_dado)
elif operacao == "*":
    resultado = abs(primeiro_dado * segundo_dado)
elif operacao == "/":
    if segundo_dado != 0:  # Verificar se o segundo dado não é zero para evitar divisão por zero
        resultado = abs(primeiro_dado / segundo_dado)
    else:
        resultado = "Erro: divisão por zero"
else:
    resultado = "Operação inválida"

# Exibir o resultado
print("O resultado em valor absoluto é:", resultado)