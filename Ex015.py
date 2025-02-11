# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
celsius = float(input("Digite uma temperatura em Celsius: "))
fahrenheit = celsius * 1.8 + 32

print ('A temperatura em Fahrenheit é {}°F'.format(fahrenheit))