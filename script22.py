# Ao desenvolver um programa, precisamos procurar na documentação da biblioteca, do módulo ou da própria linguagem de programação se as funcionalidades que vamos utilizar têm exceções mapeadas. Essas exceções são problemas que podem ocorrer, e é nossa tarefa tratá-las.
# Você deve estar se perguntando: “O que seria ‘tratar uma exceção?”. Isso nada mais é do que dizer ao Python o que fazer, ou quais instruções executar, quando ele encontrar um problema.
# Para ilustrar, observe os seguintes passos:
# 1. Quando abrimos um arquivo em modo leitura e esse arquivo não existe, o Python lança uma exceção do tipo FileNotFoundError.
# 2. Se não avisarmos ao Python o que fazer quando isso ocorrer, o programa será interrompido.
# 3. Nesse caso, um tratamento para essa exceção poderia ser: exibir um pop-up ao usuário informando que o arquivo não existe.
# Veja o que acontece quando uma exceção lançada não é tratada:

print("Abrindo um arquivo")

open("teste.txt", 'r')

print("Arquivo aberto")

# Para resolver isso, precisamos tratar a exceção, ou melhor, uma possível exceção. Esse tratamento informa ao Python uma rota alternativa, caso ele encontre um problema.
# Para tratar exceções, precisamos “envolver” o trecho de código passível de erro com a cláusula try/except ou try/except/finally. Veremos apenas a cláusula try/except.