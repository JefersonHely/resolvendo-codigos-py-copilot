# Testar se uma palavra é um palíndromo.

# Receber a palavra como entrada do usuário
palavra = input("Digite uma palavra: ")

# Converter a palavra para letras minúsculas (opcional, para considerar maiúsculas e minúsculas iguais)
palavra = palavra.lower()

# Verificar se a palavra é um palíndromo
if palavra == palavra[::-1]:
    print("A palavra é um palíndromo.")
else:
    print("A palavra não é um palíndromo.")