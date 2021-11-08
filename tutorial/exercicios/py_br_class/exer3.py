'''
Classe Retangulo: Crie uma classe que modele um retangulo:
Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. 
Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias 
para o local.
'''



class Retangulo:
    def __init__(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB

    def mudarLadoA(self, ladoA):
        self.ladoA = ladoA

    def mudarLadoB(self, ladoB):
        self.ladoB = ladoB

    def mostrarLadoA(self):
        print(self.ladoA)

    def mostrarLadoB(self):
        print(self.ladoB)

    def calcularArea(self):
        return self.ladoA * self.ladoB

    def calcularPerimetro(self):
        return (self.ladoA * 2) + (self.ladoB * 2)
        


print('Digite as medidas do local em metros:')
ladoA = float(input('Lado A: '))
ladoB = float(input('Lado B: '))
local = Retangulo(ladoA, ladoB)

print('\nDigite a medida dos materias em metros:')
pisoA = float(input('comprimento do Piso: '))
pisoB = float(input('largura do Piso: '))
roda_pe = float(input('comprimento da Rodape: '))
piso = Retangulo(pisoA, pisoB)


while piso.calcularArea() < local.calcularArea():
    piso.mudarLadoA(piso.ladoA + pisoA)
    piso.mudarLadoB(piso.ladoB + pisoB)

quantidade_pisos = piso.calcularArea() / (pisoA * pisoB)
print('\nQuantidade de pisos: ', quantidade_pisos)

total_roda_pe = roda_pe
while total_roda_pe < local.calcularPerimetro():
    total_roda_pe += roda_pe

quantidade_roda_pe = total_roda_pe / roda_pe
