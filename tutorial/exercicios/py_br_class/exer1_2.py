'''
Classe Bola: Crie uma classe que modele uma bola:
Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor

Classe Quadrado: Crie uma classe que modele um quadrado:
Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
'''



class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, cor):
        self.cor = cor
        print('Cor alterada para:', self.cor)

    def mostraCor(self):
        print('Cor da bola:', self.cor)


class Quadrado:
    def __init__(self, tamanho):
        self.tamanho = tamanho

    def mudarTamanho(self, tamanho):
        self.tamanho = tamanho
        print('Tamanho alterado para:', self.tamanho)

    def mostrarTamanho(self):
        print('Tamnho das arestas:', self.tamanho)

    def calcularArea(self):
        area = self.tamanho ** 2
        print('Area do quadrado:', area)


bola = Bola('azul', 20, 'plastico')
bola. mostraCor()
bola.trocaCor('vermelha')
bola.mostraCor()

quadrado = Quadrado(10)
quadrado.mostrarTamanho()
quadrado.calcularArea()
quadrado.mudarTamanho(20)
quadrado.mostrarTamanho()
quadrado.calcularArea()
