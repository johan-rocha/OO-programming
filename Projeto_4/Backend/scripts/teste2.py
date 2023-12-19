import numpy as np
import constants



SCALE = 2 #trabalharei com essa escala fixa

matriz_width = int(constants.WIDTH*SCALE)
matriz_height = int(constants.HEIGHT*SCALE)
matriz = np.ones((matriz_height, matriz_width), dtype=int)
print(f"x matriz = {matriz.shape[1]} y matriz = {matriz.shape[0]}")


##modificação da matriz -> define area jogavel e pellets

#[pos_linha,pos_coluna,comprimento]
linhas_paralelas = [[11, 11, 89], [43, 11, 106], [67, 11, 41], [163, 11, 25], [67, 75, 25], [91, 75, 39], [115, 0, 76], [139, 75, 39], [163, 11, 89], [187, 11, 17], [187, 51, 63], [211, 11, 41], [211, 75, 25], [235, 11, 105]]

colunas_paralelas = [[11, 11, 57], [211, 11, 25], [187, 27, 25], [11, 51, 201], [43, 75, 25], [91, 75, 73], [187, 75, 25], [11, 99, 33], [67, 99, 25], [163, 99, 25], [211, 99, 25], [163, 11, 25]]
#]

#define escala
for linha in linhas_paralelas:
    for i in range(3):
        linha[i] *= SCALE
for coluna in colunas_paralelas:
    for j in range(3):
        coluna[j] *= SCALE

# Define as linhas

for linha, inicio, comprimento in linhas_paralelas:
    comprimento -= 1 #definir proporcao -> comprimento da linha/comprimento da tela
    matriz[linha, inicio:(inicio + comprimento)] = 0
    matriz[linha, (matriz_width - inicio - comprimento):(matriz_width - inicio)] = 0

# Define as colunas da matriz e linhas do jogo
for inicio, coluna, comprimento in colunas_paralelas:
    comprimento -= 2
    matriz[inicio:(inicio + comprimento), coluna] = 0
    matriz[inicio:(inicio + comprimento), (matriz_width - coluna - 1)] = 0


######################


matriz.tofile("map.bin")



def checkColision(obj_position : tuple[int, int]):
    row, col = int(obj_position[0]), (obj_position[1])
    position = int(row * constants.WIDTH*SCALE + col)
    offset = int(position * np.dtype(int).itemsize)

    with open("map.bin", 'rb') as file:
        file.seek(offset)
        estado_colisao = np.fromfile(file, dtype=int, count=1)
    return estado_colisao.item()

posicao_coluna = 422
posicao_linha = 22


if(checkColision((posicao_linha, posicao_coluna))):
    print("verificador 2 = COLISAO")
else:
    print("verificador 2 = NAO COLIDIU PORA")