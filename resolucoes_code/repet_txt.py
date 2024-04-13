# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

# Solicitar uma string e um número inteiro como entrada
texto = input("Digite uma string: ")
numero_repeticoes = int(input("Digite um número inteiro: "))

# Verificar se o número de repetições é válido (positivo)
if numero_repeticoes > 0:
    # Repetir a string o número de vezes informado com espaço entre as palavras
    resultado = (texto + " ") * numero_repeticoes
    # Remover o espaço extra no final da string
    resultado = resultado.strip()
    # Exibir o resultado
    print("O resultado é:", resultado)
else:
    print("O número de repetições deve ser um valor inteiro positivo.")