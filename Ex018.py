'''
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
Calcule e mostre o comprimento da hipotenusa.
'''

from math import hypot
catop = float(input('Digite o comprimento do cateto oposto: '))
catad = float(input('Digite o comprimento do cateto adjacente: '))
hip = hypot(catop,catad)

print('Um triângulo com o cateto oposto {} e o cateto adjacente {}, tem sua hipotenusa valendo {:.2f}'.format(catop, catad, hip))