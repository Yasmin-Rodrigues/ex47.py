from datetime import date
menores = 0
maiores = 0
ano = date.today().year
for c in range(1, 8):
    nasc= int(input('Digite o ano de nascimento:'))
    if ano - nasc < 18:
        menores +=1
    else:
        maiores +=1
print(f'Do total de 7 pessoas, {menores} são menores e {maiores} são maiores')