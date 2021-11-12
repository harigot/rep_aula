'''
Classe Ponto e Retangulo: Faça um programa completo utilizando funções e classes que:

a. Possua uma classe chamada Ponto, com os atributos x e y.
b. Possua uma classe chamada Retangulo, com os atributos largura e altura.
c. Possua uma função para imprimir os valores da classe Ponto
d. Possua uma função para encontrar o centro de um Retângulo.
e. Você deve criar alguns objetos da classe Retangulo.
f. Cada objeto deve ter um vértice de partida, por exemplo, o vértice inferior esquerdo do retângulo, 
que deve ser um objeto da classe Ponto.
g. A função para encontrar o centro do retângulo deve retornar o valor para um objeto do tipo ponto que 
indique os valores de x e y para o centro do objeto.
h. O valor do centro do objeto deve ser mostrado na tela
i. Crie um menu para alterar os valores do retângulo e imprimir o centro deste retângulo.
'''



class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'the center is at the point: ({self.x}, {self.y})'

class rectangle:
    def __init__(self, width = 0, height = 0):
        self.width = width
        self.height = height

    def __str__(self):
        return f'({self.width}, {self.height})'
    
    def change_size(self, width, height):
        self.width = width
        self.height = height

    def center(self):
        rectangle_center = point(self.width/2, self.height/2)
        rectangle_center.__str__()


rectangle1 = rectangle(10, 20)
rectangle2 = rectangle(30, 40)
rectangle3 = rectangle(50, 60)

rectangle1.center()

rectangle1.change_size(20, 30)
rectangle1.center()
print(rectangle1)
