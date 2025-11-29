#Laços de repetição (for e while)

#exemplo 1 com for
for numero in range(1, 6):
    print(numero)


# #exemplo 2 com for
compras = ["maçã", "banana", "laranja", "abacaxi", "melancia"]
for item in compras:
    print(f"comprar {item}")

#exemplo 3 com for
palavra = "Python"
for letra in palavra:
    print(letra)


#exemplo 1 com while
contador = 10
while contador > 0:
    print(contador)
    contador -= 1
print("Feliz Ano Novo!")


#exemplo 2 com while
senha_correta = "root123"
senha = ""

while senha != senha_correta:
    senha = input("Digite a senha: ")
print("Acesso concedido!")