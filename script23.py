
# O código crítico que desejamos executar deve estar no escopo do try, enquanto o código alternativo, que será executado em caso de erro, deve estar no escopo do except. 
# Uma mesma operação pode lançar mais de um tipo diferente de exceção, em que, para cada tipo, Erro1 e Erro2, devemos ter uma cláusula except específica.
# No exemplo da imagem, a exceção está disponível por meio da variável erro, de onde podemos extrair mais informações, como veremos a seguir.
# Praticamente todas as exceções em Python são herdadas da classe Exception, ou seja, ela é uma exceção muito genérica, lançada por diversos tipos de erros diferentes. Quanto mais genérica, mais abrangente é a exceção.

# Confira algumas exceções específicas relacionadas à manipulação de arquivos e alguns motivos que podem gerar essas exceções:
# PermissionError: Lançada quando não temos permissão para realizar uma operação.
# FileExistsError: Lançada quando tentamos criar um arquivo ou diretório já existentes.
# FileNotFoundError: Lançada quando tentamos abrir um arquivo ou diretório que não existem.

# Todas essas exceções herdam da exceção mais abrangente OSError, que, por sua vez, herda de Exception.
# Observe o exemplo a seguir, onde vamos tratar a exceção do exemplo anterior, utilizando a exceção específica mais indicada: FileNotFoundError:

# Durante a execução do programa, ao executar a linha 4, o Python encontra um erro, pois tentamos abrir o arquivo teste.txt para leitura, mas ele não existe. Como este código está dentro do escopo do try, o interpretador interrompe imediatamente a execução do código contido nesse escopo e inicia a execução do código do except correspondente ao erro FileNotFoundError. Ou seja, a execução salta da linha 4 para a linha 7.
# Na linha 7, imprimimos a mensagem "Arquivo inexistente" e, na linha 8, imprimimos o problema encontrado, disponível na variável erro.

print("Abrindo um arquivo")

try:
    open("teste.txt", 'r')
    print("Arquivo aberto!")
except FileNotFoundError as erro:
    print("Arquivo não encontrado!")
    print("Descrição:", erro)

print("Continuando o programa...")

# Saiba que o Python só consegue tratar a exceção caso o erro esteja mapeado em algum except. Se o interpretador não encontrar o except adequado, será gerado um erro, e o programa será interrompido.
# Um problema clássico que ocorre quando lidamos com arquivos é tentar alterar o conteúdo de um arquivo quando ele está aberto em outro programa. No caso do sistema operacional Windows 10, é lançada uma exceção sobre permissão de acesso.
# A seguir, vamos criar mais um except para tratar o caso de não termos permissão para abrir um arquivo, mostrando o tratamento do problema levantado no parágrafo anterior.