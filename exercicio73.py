brasileirao = ('palmeiras', 'internacional', 'flamengo', 'fluminense', 'corinthians', 'atlético-PR', 'atlético-MG',
 'américa- MG', 'goiás', 'santos', 'bragantino', 'botafogo', 'são paulo')

print(f'Os 5 primeiros classificados do brasileirão são {brasileirao[0:6]}')
print("==========================================================")
print(f'Os 5 últimos da tabela do brasileirão são: {brasileirao[8:]}')
print("==========================================================")
print(f'Tabela do brasileirão: {sorted(brasileirao)}')
print("==========================================================")
print(brasileirao.index('santos')+1)