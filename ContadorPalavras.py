def contar_palavras(texto):
    palavras = texto.split()
    return len(palavras)

frase = input("Digite um texto: ")
print(f"O texto contém {contar_palavras(frase)} palavras.")