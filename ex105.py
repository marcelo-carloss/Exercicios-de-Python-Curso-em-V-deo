def notas(*num,sit=False):
  """
  -> Função para analisar notas e situações de vários alunos.
  :param num: uma ou mais notas dos alunos (aceita várias)
  :param sit: valor opcional, indicando se deve ou não adicionar a situação.
  :return: dicionário com várias informações sobre a situação da turma. 
  """
  notas = dict()
  notas['total'] = len(num)
  notas['maior'] = max(num)
  notas['menor'] = min(num)
  notas['media'] = sum(num) / len(num)
  if sit == True:
    if notas['media'] > 6.9:
      notas['situação'] = 'BOA'
    elif notas['media'] < 4.5:
      notas['situação'] = 'RUIM'
    else:
      notas['situação'] = 'REGULAR'
  return notas

resposta = notas(6, 5, 3, 7, 10, 2)
print(resposta)
  
