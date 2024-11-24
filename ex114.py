import urllib
import urllib.error
import urllib.request
try:
  site = urllib.request.urlopen('https://www.youtube.com.br')
except urllib.error.URLError:
  print('\033[0;31mNão consegui acessar o site do PUDIM!\033[m')
else:
  print('\033[0;32mConsegui acessar o site do PUDIM com sucesso!\033[m')


