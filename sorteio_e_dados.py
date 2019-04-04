import random
from time import sleep
from operator import itemgetter
#print (random.randint(0,5))
dado = dict()
dados = {
  'jogador 1' : random.randint(1,6),
  'jogardor 2' : random.randint(1,6),
  'jogador 3' : random.randint(1,6),
  'jogador 4' : random.randint(1,6)
}
rankin = list()
print ('=+'*10," Valores Sorteados ", '=+'*10)
print ('\n')
for k,v in dados.items():
  print (' '*20,f'{k} Tirou {v} no dado.\n')
  sleep(1)

print ('=*'10,' PROCESSANDO OS DADOS ', '='*10)

sleep (2)

rankin = sorted (dados.items(), key = itemgetter(1), reverse = True)
print (' '*20, ' Classificação Geral.\n')
for m,n in enumerate(rankin):
  print (f'                 {m+1}º lugar: {n[0]} com {n[1]}\n')
