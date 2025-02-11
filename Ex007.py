#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n1= int(input('Digite um número: '))
dobro= n1*2
triplo = n1*3
raiz = n1 **(1/2)

print('O número escolhido foi {}, \nSeu dobro é {}, \nSeu triplo é {}, \nSua raiz quadrada é {}'.format(n1, dobro, triplo, raiz))