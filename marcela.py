#Exercício Python 28 : Crie um programa que leia o ano de nascimento de sete pessoas. No final,
# mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date

today = date.today()
anoatual = today.year

MAIORESIDADE = []
MENORESIDADE = []

for item in range(8):
  anoNascimento = int(input('Insira o ano de nascimento: '))
  if anoatual - anoNascimento >= 18:
   MAIORESIDADE.append(anoNascimento)
  else:
   MENORESIDADE.append(anoNascimento)

print('Maiores de idade:' , MAIORESIDADE)
print('Menores de idade:' , MENORESIDADE)