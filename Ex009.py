#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

valor = float(input('Quantos metros você tem? '))
cm = valor * 100
mm = valor * 1000

print('Seu tamanho em centímetros é {}, e em milímetros é {}'.format(cm,mm))