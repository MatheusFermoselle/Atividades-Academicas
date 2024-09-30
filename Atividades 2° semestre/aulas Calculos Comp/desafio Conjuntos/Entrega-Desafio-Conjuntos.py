import psutil as p
import math as m
# 2. Converta os portfolios em conjuntos
conjAgora = {'Itaúsa','Ecorodovias', 'Taesa', 'B3', 'Vale'}
conjAtiva = {'B3', 'Bradesco', 'BB Seguridade', 'BR Distribuidora', 'Taesa', 'CTEEP', 'Vale', 'Telefônica Brasil'}
conjGenial = {'CPFL', 'Minerva', 'Cyrela', 'Randon', 'CTEEP'}
conjEasynvest = {'B3', 'Brasil Agro', 'Coca-cola', 'Taesa', 'Vale', 'Copel', 'Itaúsa', 'Ambev'}
conjElite = {'Bradesco', 'BB Seguridade', 'Banrisul', 'Engie', 'Itaúsa', 'Sanepar', 'Taesa', 'CTEEP', 'Telefônica Brasil', 'Vale'}
conjGuide = {'Alupar', 'Banco do Brasil', 'Cyrela', 'CPFL', 'Klabin', 'Porto Seguro', 'Tim', 'Vale',}
conjNovaFutura = {'B3', 'Cyrela', 'Gerdau', 'Vivo', 'CTEEP'}
conjOrama = {'Banco ABC', 'Bradesco', 'Minerva', 'CESP', 'Engie'}
# 3. Ache se há alguma ação em comum a todas a corretoras
#    -> Não exite nenhuma empresa que esteja em todas corretoras
relacaoTodas = conjAtiva & conjGenial & conjEasynvest & conjElite & conjGuide & conjNovaFutura & conjOrama
print(relacaoTodas)
# 4. Selecione 4 corretoras (seu critério)
# a) Ache se há alguma ação em comum a essas 4 corretoras
relacaoQuatro = conjAtiva & conjElite & conjNovaFutura & conjGenial
print(relacaoQuatro)
# b) Indique se há ações únicas para cada corretora 
diferencaQuatro = conjAtiva ^ conjElite ^ conjNovaFutura ^ conjGenial
print(diferencaQuatro)
# c) Determine as relações entre os portfólios das corretoras (subset ou superset) 
print(conjAtiva.issubset(conjElite | conjNovaFutura | conjGenial))
print(conjAtiva.issuperset(conjElite | conjNovaFutura | conjGenial))
print(conjElite.issubset(conjAtiva | conjNovaFutura | conjGenial))
print(conjElite.issuperset(conjAtiva | conjNovaFutura | conjGenial))
print(conjGenial.issubset(conjElite | conjNovaFutura | conjAtiva))
print(conjGenial.issuperset(conjElite | conjNovaFutura | conjAtiva))
print(conjNovaFutura.issubset(conjElite | conjGenial | conjAtiva))
print(conjNovaFutura.issuperset(conjElite | conjGenial | conjAtiva))
# d) Crie um conjunto de ações únicos de cada corretora
acaoUnicaAtiva = conjAtiva - (conjElite  | conjNovaFutura | conjGenial)
print(acaoUnicaAtiva)
acaoUnicaElite = conjElite - (conjAtiva  | conjNovaFutura | conjGenial)
print(acaoUnicaElite)
acaoUnicaNovaFutura = conjNovaFutura - (conjElite  | conjAtiva | conjGenial)
print(acaoUnicaNovaFutura)
acaoUnicaGenial = conjGenial - (conjElite  | conjNovaFutura | conjAtiva)
print(acaoUnicaGenial)




