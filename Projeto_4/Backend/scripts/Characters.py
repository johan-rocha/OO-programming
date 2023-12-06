import abc #Abstract Base Classes

class Characters(abc.ABC): #abstract class
    #speed
    #name
    #color
    #direction
    def __init__(self):
        pass

    @abc.abstractmethod #ver como funciona, usando como exemplo
    def setSpeed():
        pass

class Pacman(Characters): #definir classe
    def __init__(self):
        pass

class Ghost(Characters): #definir classe
    def __init__(self):
        pass