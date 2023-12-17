import numpy as np
import constants



SCALE = 1

smallest_wall_block_size = 4*SCALE
matriz_width = int(constants.WIDTH*SCALE)
matriz_height = int(constants.HEIGHT*SCALE)
matriz = np.zeros((matriz_height, matriz_width), dtype=int)
#block = np.ones((int(4 * constants.SCALE), int(4 * constants.SCALE)), dtype=int)
print(f"x matriz = {matriz.shape[1]} y matriz = {matriz.shape[0]}")

#multiplicar tudo depois por escala
# i-> linha j->coluna

for i in range(80*SCALE): #RED
    for j in range(smallest_wall_block_size):
        matriz[i, j] = 1
        matriz[i, (matriz_width-1)-j] = 1

for i in range(152*SCALE, matriz_height): #RED
    for j in range(smallest_wall_block_size):
        matriz[i, j] = 1
        matriz[i, (matriz_width-1)-j] = 1

for i in range(80*SCALE, 104*SCALE): #RED
    for j in range(smallest_wall_block_size):
        matriz[i, 40*SCALE+j] = 1
        matriz[i, (matriz_width-1)-(40*SCALE+j)] = 1
        matriz[i+48*SCALE, 40*SCALE+j] = 1 #i + ...
        matriz[i+48*SCALE, (matriz_width-1)-(40*SCALE+j)] = 1

for i in range(smallest_wall_block_size): #RED
    for j in range(matriz_width): #consertando
        matriz[i, j] = 1
        matriz[(matriz_height-1)-i, j] = 1

for i in range(smallest_wall_block_size): #RED
    for j in range(44*SCALE): #correto
        matriz[76*SCALE+i, j] = 1 #
        matriz[76*SCALE+i, (matriz_width-1)-j] = 1
        matriz[76*SCALE+i+28*SCALE, j] = 1 #
        matriz[76*SCALE+i+28*SCALE, (matriz_width-1)-j] = 1
        matriz[76*SCALE+i+48*SCALE, j] = 1 #
        matriz[76*SCALE+i+48*SCALE, (matriz_width-1)-j] = 1
        matriz[76*SCALE+i+76*SCALE, j] = 1 #
        matriz[76*SCALE+i+76*SCALE, (matriz_width-1)-j] = 1


for i in range(20): #YELLOW #nao funcionou
    for j in range(20, 44):
        matriz[i, j] = 1
        matriz[i, (matriz_width-1)-j] = 1
    
    for j in range(60, 92):
        matriz[i, j] = 1
        matriz[i, (matriz_width-1)-j] = 1


matriz.tofile("map.bin")


derived_matriz = np.fromfile("map.bin", dtype=int).reshape((matriz_height, matriz_width))


""" with open("map.bin", 'wb') as file:
    for linha in matriz:
        file.write(linha.tobytes()) """


"""
for i in range(matriz.shape[0]):
    for j in range(matriz.shape[1]):
        print(matriz[i][j], end=" ")
    print("")

print(matriz)
 """

print(derived_matriz)

posicao_coluna = 20
posicao_linha = 20


with open("map.bin", 'rb') as file:
    file.seek((posicao_linha * matriz_width + posicao_coluna) * matriz.itemsize)
    elemento = np.fromfile(file, dtype=int, count=1)

print(f"elemento = {elemento}")

