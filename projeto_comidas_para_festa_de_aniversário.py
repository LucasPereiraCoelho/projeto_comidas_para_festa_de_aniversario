#Crie um programa que permita o usuário encomendar comidas de aniversário.
#Cada item tem um pedido mínimo.

#MENU

#Bolo - R$50 o quilo - peso mínimo 1,5kg
#Torta - R$70 o quilo - peso mínimo 1kg

#Salgados:

#1)Frito - R$80 o cento - mínimo 20 unidades de cada. Opções:

#a)Bolinha de queijo
#b)Pastel de carne
#c)Coxinha

#2)Assado - R$100 o cento - mínimo 20 unidades de cada. Opções:

#a)Legumes
#b)Brócolis
#c)Camarão

#3)Folhado - R$120 o cento - mínimo 20 unidades de cada. Opções:

#a)Frango
#b)Palmito
#c)Queijo e Presunto

#Docinho: 

#1)Simples - R$100 o cento - mínimo 25 unidades. Opções:

#a)Brigadeiro
#b)Casadinho
#c)Cajuzinho

#2)Especial - R$150 o cento - mínimo 25 unidades. Opções:

#a)Leite ninho com nutella
#b)Churros
#c)Brigadeiro vegano.

print("Bolo - R$50 o quilo - peso mínimo 1,5kg")
print("Torta - R$70 o quilo - peso mínimo 1kg")

bolo = float(input("Informe a quantidade de bolo necessária em Kg: "))
torta = float(input("Informe a quantidade de torta necessária em Kg: "))


print("Salgados Fritos - R$80 o cento - mínimo 20 unidades de cada.")
bolinhaqueijo = int(input("Quantas bolinhas de queijo: "))
pastelcarne = int(input("Quantos pastéis de carne: "))
coxinha = int(input("Quantas coxinhas: "))
totalfritos = bolinhaqueijo + pastelcarne + coxinha


print("Assado - R$100 o cento - mínimo 20 unidades de cada.")
legumes = int(input("Quantos assados de legumes: "))
brocolis = int(input("Quantos assados de brócolis: "))
camarao = int(input("Quantos assados de camarão: "))
totalassados = legumes + brocolis + camarao


print("Folhado - R$120 o cento - mínimo 20 unidades de cada.")
frango = int(input("Quantos salgados de frango folhado: "))
palmito = int(input("Quantos salgados de palmito: "))
queijopresunto = int(input("Quantos salgados de queijo e presunto: "))
totalfolhados = frango + palmito + queijopresunto


print("Docinhos Simples - R$100 o cento - mínimo 25 unidades totais.")
brigadeiro = int(input("Quantos brigadeiros: "))
casadinho = int(input("Quantos casadinhos: "))
cajuzinho = int(input("Quantos cajuzinhos: "))
totaldocesimples = brigadeiro + casadinho + cajuzinho


print("Docinhos Especiais - R$150 o cento - mínimo 25 unidades totais.")
leitenutela = int(input("Quantos doces de leite com Nutella: "))
churros = int(input("Quantos doces de churros: "))
brigadeirovegano = int(input("Quantos brigadeiros veganos: "))
totaldoceespecial = leitenutela + churros + brigadeirovegano


frasebolotorta = "A quantia de bolo requisitada foi de {}Kg e dará {} reais, e de torta a quantia especificada foi de {}Kg dando {} reais ".format(bolo, bolo * 50, torta, torta * 70)
frasefritos = "Foi pedido um total de {} salgados fritos, sendo 80 reais o cento, dando um total de {}".format(totalfritos, (totalfritos / 100) * 80)
fraseassados = "Foi pedido um total de {} salgados assados, sendo 100 reais o cento, dando um total de {}".format(totalassados, (totalassados / 100) * 100)
frasefolhados = "Foi pedido um total de {} salgados folhados, sendo 120 reais o cento, dando um total de {}".format(totalfolhados, (totalfolhados / 100) * 120)
frasedocesimples = "Foi pedido um total de {} docinhos simples, sendo 100 reais o cento, dando um total de {}".format(totaldocesimples, (totaldocesimples / 100) * 100)
frasedoceespecial = "Foi pedido um total de {} docinhos especiais, sendo 150 reais o cento, dando um total de {}".format(totaldoceespecial, (totaldoceespecial / 100) * 150)

print(frasebolotorta)
print(frasefritos)
print(fraseassados)
print(frasefolhados)
print(frasedocesimples)
print(frasedoceespecial)