#CONDICIONAIS

#exemplo pratico 1:
altura = float (input("Qual sua altura?: ")) #verificiar se a pessoal tem altura para ir em um brinquedo

if altura >=1.60:
    print("Oba, você pode entrar no brinquedo")
elif altura >=1.50:
    print("Pode entrar no brinquedo com a supervisão de um adulto")
else:
    print("Desculpe, mas você não pode entrar no brinquedo")


# #exemplo pratico 2:
idade = int(input("Qual sua idade?: ")) #verificar se a pessoa pode tirar a carteira de motorista

if idade >= 18:
    print("Parabens!!, você pode tirar a carteira de motorista")
else:
    print("Desculpe, mas você ainda nã tem idade suficiente para tirar a carteira de motorista")


#exemplo pratico 3:
resposta = input("Você foi aprovado? (s/n): ") #verificar o resulatdo na escola

aprovado = "s"

if resposta == "s":
    print("Parabéns! Você passou!")
else:
    print("Não foi dessa vez, tente novamente no próximo ano.")