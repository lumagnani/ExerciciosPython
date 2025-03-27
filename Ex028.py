'''
Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente.
'''

nome_completo = input("Digite seu nome completo: ").strip()
nomes = nome_completo.split()

primeiro_nome = nomes[0]
ultimo_nome = nomes[-1]

print(f"Primeiro nome: {primeiro_nome}")
print(f"Último nome: {ultimo_nome}")
