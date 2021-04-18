print('Programa minha idade')

idade = input('Qual a sua idade? ')
print('Sua idade é', idade)

maior_ou_menor = ''
if int(idade) >= 18:
    maior_ou_menor = 'maior'
else:
    maior_ou_menor = 'menor'

print('Voce é', maior_ou_menor, 'idade')