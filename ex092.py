from datetime import datetime
aposentar = {}
aposentar['nome'] = str(input('Seu nome: '))
anoNas= int(input('Ano de nascimento: '))
aposentar['ctps'] = int(input('Sua Carteira de Trabalho (0 se não tiver): '))
aposentar['idade'] = datetime.now().year - anoNas
if aposentar['ctps'] != 0:
  aposentar['anoCon'] = int(input('Qual foi o ano da sua contratação? '))
  aposentar['salario'] = float(input('Qual seu salário? R$'))
  aposentar['idadeApo'] = (aposentar['anoCon'] + 35) - anoNas
print(f'Nome: {aposentar["nome"]}')
print(f'Idade: {aposentar["idade"]} anos')
print(f'ctps: {aposentar["ctps"]}')
if aposentar['ctps'] != 0:
  print(f'Sálario: {aposentar["salario"]}')
  print(f'Idade de Aposentadoria: {aposentar["idadeApo"]} anos')
print(aposentar)