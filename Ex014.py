#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Qual o seu salário atual? '))
novo = salario * 1.15

print('Com um aumento de 15%, seu novo salário é de R${:.2f}'.format(novo))