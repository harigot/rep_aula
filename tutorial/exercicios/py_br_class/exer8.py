'''
Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago) e pelo menos 
os métodos comer(), verBucho() e digerir(). Faça um programa ou teste interativamente, criando pelo 
menos dois macacos, alimentando-os com pelo menos 3 alimentos diferentes e verificando o conteúdo do 
estomago a cada refeição. Experimente fazer com que um macaco coma o outro. É possível criar um macaco 
canibal?
'''



class Mankey:
    def __init__(self, name, stomach = []):
        self.name = name
        self.stomach = stomach 

    def eat(self, food):
        self.stomach.append(food)
    
    def see_stomach(self):
        if len(self.stomach) > 0:
            print(self.stomach)
        else:
            print(f'My stomach is empty! {self.name} demands food!')
    
    def digest(self):
        self.stomach.clear()


kong = Mankey('Kong')
kerchak = Mankey('Kerchak')

kong.see_stomach()
kong.eat('banana')
kong.eat(kerchak)
kong.eat('apple')
kong.see_stomach()
kong.digest()
kong.see_stomach()