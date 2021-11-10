'''
Classe Pessoa: Crie uma classe que modele uma pessoa:

Atributos: nome, idade, peso e altura
Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa 
envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
'''



class Person:
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def get_old(self):
        self.age += 1
        if self.age < 21:
            self.height += 0.05

    def fatten(self, weight):
        self.weight += weight

    def lose_weight(self, weight):
        self.weight -= weight

    def grow(self, height):
        self.height += height

    def display(self):
        print(f'{self.name} is {self.age} years old, weighs {self.weight} kg and is {self.height} tall.')


pesron1 = Person('John', 19, 80, 1.80)
pesron1.display()
pesron1.get_old()
pesron1.fatten(10)
pesron1.lose_weight(5)
pesron1.display()
