# 2. Funções de manipulação de strings
# Formatação de strings

# -*- coding: utf-8 -*-

nome = "Thiago"

minha_string = "Olá, " + nome + "!"
minha_fstring1 = f"Olá, {nome}!"
minha_fstring2 = f"Olá, {nome.upper()}!"
minha_fstring3 = f"Quantos anos você tem? {18 + 10}."
minha_fstring4 = f"O número 2 é maior que o número 1? {2 > 1}."
minha_fstring5 = f"O número 2 está contido na lista [4, 5, 6]? {2 in [4, 5, 6]}."

print(minha_string)
print(minha_fstring1)
print(minha_fstring2)
print(minha_fstring3)
print(minha_fstring4)
print(minha_fstring5)