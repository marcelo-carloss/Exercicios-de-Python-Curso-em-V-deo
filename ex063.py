f = [0,1]
num = int(input('Digite quantos elementos da Sequência de Fibonacci você deseja ver: '))
for i in range(f[0], num - 2):
  f.append(f[i] + f[i + 1])
print(f)


