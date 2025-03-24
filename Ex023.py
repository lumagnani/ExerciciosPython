'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiúsculas e minúsculas.
Quantas letras ao todo sem considerar espaços.
Quantas letras tem o primeiro nome.
'''
nome = input('Digite seu nome completo: ').strip()
print(nome.upper())
print(nome.lower())
print(len(nome) - nome.count(' ')) #Tirando os espaços
#print (nome.find(' '))
separa = nome.split()
print(len(separa[0]))


