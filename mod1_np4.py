# 1. Funções de manipulação de arquivos
# Lidando com dados binários em arquivo com Python

from PIL import Image
import numpy as np

def carregar_imagem(caminho):
    try:
        return Image.open(caminho)
    except FileNotFoundError:
        print(f"Arquivo {caminho} não encontrado.")
        return None

def salvar_dados_binarios(caminho, dados):
    with open(caminho, "wb") as file:
        file.write(dados)

def ler_dados_binarios(caminho):
    with open(caminho, "rb") as file:
        return file.read()

def inverter_bytes(dados):
    return bytearray(dados[::-1])

def mostrar_imagem(dados, shape):
    modified_data = np.frombuffer(dados, dtype=np.uint8).reshape(shape)
    modified_data = np.fliplr(modified_data)
    modified_img = Image.fromarray(modified_data)
    modified_img.show()

def main():
    img = carregar_imagem("simple_icon.png")
    if img is None:
        return

    img_data = np.array(img)
    binary_data = img_data.tobytes()

    print("\n", img_data.shape, "\n")

    salvar_dados_binarios("original_img.bin", binary_data)
    data = ler_dados_binarios("original_img.bin")
    salvar_dados_binarios("copy_img.bin", data)

    data = ler_dados_binarios("copy_img.bin")
    data = inverter_bytes(data)
    salvar_dados_binarios("copy_img.bin", data)

    mostrar_imagem(data, img_data.shape)

if __name__ == "__main__":
    main()