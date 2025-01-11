# 3. Tratamento de exceções e outras operações
# Operações adicionais em arquivos

# Veja a função remove na imagem abaixo. Iniciamos o script com a importação do módulo os, na linha 1. Aqui vamos remover o arquivo teste.txt, 
#   que se encontra no mesmo diretório do nosso script. Observe a arvore de diretórios à esquerda:

import os

try:
    os.remove('teste.txt')
    print('Arquivo removido com sucesso!')
except FileNotFoundError as erro:
    print("Arquivo não encontrado")
    print("Descrição", erro)
except PermissionError as erro:
    print("Permissão negada")
    print("Descrição", erro)
except IsADirectoryError as erro:
    print("Remove serve apenas para arquivos")
    print("Descrição", erro)

    print("Fim do programa")


# Na linha 2, utilizamos a função remove, passando como argumento o caminho do arquivo que desejamos remover. Como estamos no mesmo diretório, utilizamos apenas o nome do arquivo. Pronto! Isso é suficiente para remover um arquivo.
# Dentre as exceções lançadas ao usar a função remove, destacamos as seguintes:

# FileNotFoundError
# Ocorre quando o arquivo não existe.

# PermissionError
# Ocorre quando não temos permissão para alterar o arquivo.

# IsADirectoryError
# Ocorre quando tentamos remover um diretório usando a função remove, em vez de rmdir.

# Observe a saída do console, onde tudo ocorreu conforme esperado e nenhuma exceção foi lançada.
# A segunda operação, também muito comum, é a de renomear um arquivo. Essa operação também está disponível no módulo os, mas por meio da função rename.