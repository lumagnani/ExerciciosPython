#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
valor = float(input('Digite o valor do produto em R$'))
desconto = (valor * 0.95)

print('O produto está com desconto de 5%! Seu novo valor é de R${:.2f}'.format(desconto))