def zenit_polar_replace(text):
    # Aplicar a codificação Z-E-N-I-T-E-T-P-O-L-A-R Utilizando o método replace
    replacements = [('z', 'p'), ('e', 'o'), ('n', 'l'), ('i', 'a'), ('t', 'r'), ('p', 'z'), ('o', 'e'), ('l', 'n'), ('a', 'i'), ('r', 't'), # Minusculas
                    ('Z', 'P'), ('E', 'O'), ('N', 'L'), ('I', 'A'), ('T', 'R'), ('P', 'Z'), ('O', 'E'), ('L', 'N'), ('A', 'I'), ('R', 'T')] # Maiusculas
    for old, new in replacements:
        text = text.replace(old, new)
    return text
    
def main():
    # Entrada da frase e aplicação da codificação
    phrase = "The quick brown fox jumps over the lazy dog"
    phrase_title = phrase.title() # Primeira letra de cada palavra em maiúscula

    # Dividir a frase em palavras
    words = phrase_title.split()

    # Processar cada palavra na lista usando ZENIT POLAR
    coded_words = [zenit_polar_replace(word) for word in words]

    # Juntas todas as palavras codificadas em uma frase
    coded_phrase = " ".join(coded_words)
    print("Original:", phrase)
    print("Title:", phrase_title)
    print("Coded:", coded_phrase)

if __name__ == "__main__":
    main()