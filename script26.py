# A função rename tem a seguinte sintaxe:
# >>> os.rename(origem, destino)

# Nesse exemplo, temos o nome do módulo os, seguido de um ponto e o nome da função rename. Como parâmetro, a função espera o caminho para o arquivo que desejamos renomear, origem, e o novo nome do arquivo, destino.

import os

try:
    os.rename("teste_alfa.txt", "teste_beta.txt")
    print('Arquivo renomeado com sucesso!')
except FileNotFoundError as erro:
    print("Arquivo não encontrado")
    print("Descrição", erro)
except PermissionError as erro:
    print("Permissão negada")
    print("Descrição", erro)
except FileExistsError as erro:
    print("Arquivo de destino já existe")
    print("Descrição", erro)

print("Fim do programa")

# Na linha 1, importamos o módulo os, no qual será utilizada a função rename.
# Na linha 4, chamamos a função rename com os parâmetros teste_alfa.txt (origem) e teste_beta.txt (destino). Caso tudo ocorra bem, ao final da operação, teremos apenas o arquivo destino.
# Veja agora algumas exceções que podem ser lançadas quando utilizamos a função rename. Não estamos tratando todas as opções possíveis, mas apenas as mais comuns:

# FileNotFoundError
# Ocorre quando a origem não existe.

# FileExistsError
# Ocorre quando o arquivo de destino já existe.

# PermissionError
# Ocorre quando não temos permissão para alterar o arquivo de origem ou para escrita do destino.

# Na imagem Script 26 e sua saída, veja a árvore de diretórios à esquerda. Temos tanto o arquivo teste_alfa.txt quanto o arquivo teste_beta.txt.

# Observe a execução do script pelo console e veja que ele saltou da linha 4 para a linha 13. Isso ocorreu porque, como o arquivo teste_beta.txt já existia, a exceção FileExistsError foi lançada.

# Para os casos em que desejamos renomear sobrescrevendo o arquivo destino, caso ele exista, podemos utilizar a função replace, também do módulo os.