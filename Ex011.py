#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
print('Olá, vou te ajudar a ver quantos dólares você consegue comprar!')
carteira = float(input('Digite o valor da carteira em R$'))
dolar = carteira / 5.81

print('Você consegue comprar {:.2f} dólares!'.format(dolar))