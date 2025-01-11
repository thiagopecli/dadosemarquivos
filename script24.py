
# Neste exemplo, tentamos abrir o arquivo teste.pdf para escrita, linha 4, porém ele já está aberto em outro programa:

print("Abrindo um arquivo")

try:
    open("teste.pdf", "w")
    print("Arquivo aberto com sucesso")
except FileNotFoundError as erro:
    print("Arquivo inexistente")
    print("Descrição", erro)
except PermissionError as erro:
    print("Sem permissão para abrir o arquivo")
    print("Descrição", erro)

print("Fim do programa")

# Observe que o fluxo de execução do programa saltou da linha 4 para a linha 10. Na linha 10, temos o início do tratamento da exceção PermissionError, que foi justamente a exceção lançada pelo Python, impressa pela linha 11, e que pode ser verificada no console.
# O Python direciona o fluxo de execução para o trecho onde é realizado o tratamento da exceção lançada.