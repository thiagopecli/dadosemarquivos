# 2. Funções de manipulação de strings
# Manipulação de strings
# ARQUIVO: mod2_nc1_1.py AO mod_2_nc1_7.py

arquivo = open('dados.txt', 'r', encoding='utf-8')

conteudo = arquivo.read()

print("Tipo de conteúdo: ", type(conteudo))

print('Conteúdo retornado pelo read:')

print(repr(conteudo))

arquivo.close()