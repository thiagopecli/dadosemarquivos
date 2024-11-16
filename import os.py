import os

arquivo1 = open("arquivo1.txt", 'w', encoding='utf-8')
print(os.path.abspath(arquivo1.name))
# arquivo2 = open("E:\Documentos\FACULDADE\LABORATÓRIO\RAD - Manipulação de Dados em Arquivos/dados1.txt")
arquivo1.write("Olá, mundo!")

print(os.path.relpath(arquivo1.name))
print(arquivo1)

arquivo1.close()