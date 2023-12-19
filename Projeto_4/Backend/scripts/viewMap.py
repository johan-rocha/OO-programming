from PIL import Image
import numpy as np
import constants



def checkColision(obj_position : tuple[int, int]):
    col, row = int(obj_position[0]), (obj_position[1])
    position = int(row * constants.WIDTH*constants.SCALE + col)
    offset = int(position * np.dtype(int).itemsize)

    with open("map.bin", 'rb') as file:
        file.seek(offset)
        estado_colisao = np.fromfile(file, dtype=int, count=1)
    return estado_colisao.item()


img = Image.new("RGB", (constants.WIDTH*constants.SCALE, constants.HEIGHT*constants.SCALE), (255, 255, 255))


for x in range(constants.WIDTH*constants.SCALE):
    for y in range(constants.HEIGHT*constants.SCALE):
        if(not checkColision((x, y))):
            img.putpixel((x,y), (0,0,0))





img.save("output.jpg")