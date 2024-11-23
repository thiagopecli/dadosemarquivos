import os

# Abrindo o arquivo no modo escrita
arquivo = open('exemplo.txt', 'w', encoding='utf-8')

# Exibindo os atributos do arquivo
print("Nome do arquivo:", arquivo.name)
print("Modo de abertura:", arquivo.mode)
print("Arquivo está fechado:", arquivo.closed)

# Escrevendo no arquivo
arquivo.write("Olá, mundo!")

# Fechando o arquivo
arquivo.close()

# Verificando se o arquivo está fechado
print("Arquivo está fechado agora?", arquivo.closed)

# Exibindo caminhos relativo e absoluto
relpath = os.path.relpath('exemplo.txt')
abspath = os.path.abspath('exemplo.txt')

print("Caminho relativo:", relpath)
print("Caminho absoluto:", abspath)