import arquivo
import interface
from time import sleep

arq = 'ex115/cadastros.txt'

if not arquivo.arquivoExiste(arq):
  arquivo.criarArquivo(arq)

while True:
  opç = interface.menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Programa'])
  if opç == 1:
    #Opção de listar o conteudo de um arquivo
    arquivo.lerArquivos(arq)
  elif opç == 2:
    #Opção de cadastrar uma nova pessoa.
    interface.cabecalho('NOVO CADASTRO')
    nome = str(input('Nome: '))
    idade = interface.leiaInt('Idade: ')
    arquivo.cadastrar(arq, nome, idade)
  elif opç == 3:
    #Opção de Sair do Sistema
    interface.cabecalho('ENCERRANDO PROGRAMA')
    break
  else: 
    #Digitou uma opção errada no menu
    print('\033[0;31mERRO: Digite um número inteiro válido!\033[m')
  sleep(2)