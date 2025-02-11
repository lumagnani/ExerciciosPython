#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin ,cos, tan

angulo = float(input('Digite um angulo: '))
seno = sin(radians(angulo))
print('O ângulo {} tem o seno de {:.2f}'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('O ângulo {} tem o cosseno de {:.2f}'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('O ângulo {} tem o seno de {:.2f}'.format(angulo, tangente))
