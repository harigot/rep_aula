'''
10. Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:
a. Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
tipoCombustivel.
valorLitro
quantidadeCombustivel
b. Possua no mínimo esses métodos:
abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros 
que foi colocada no veículo
abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a 
ser pago pelo cliente.
alterarValor( ) – altera o valor do litro do combustível.
alterarCombustivel( ) – altera o tipo do combustível.
alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na 
bomba.


11. Classe carro: Implemente uma classe chamada Carro com as seguintes propriedades:

a. Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de 
combustível no tanque.
b. O consumo é especificado no construtor e o nível de combustível inicial é 0.
c. Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa distância, reduzindo 
o nível de combustível no tanque de gasolina.
d. Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
e. Forneça um método adicionarGasolina( ), para abastecer o tanque. 
Exemplo de uso:
meuFusca = Carro(15);           # 15 quilômetros por litro de combustível. 
meuFusca.adicionarGasolina(20); # abastece com 20 litros de combustível. 
meuFusca.andar(100);            # anda 100 quilômetros.
meuFusca.obterGasolina()        # Imprime o combustível que resta no tanque.
'''



class FuelPump:
    def __init__(self, fuel_type, fuel_price,):
        self.fuel_type = fuel_type
        self.fuel_price = fuel_price
        self.fuel_level = 100

    def __str__(self):
        return f'Fuel price: R${self.fuel_price}\nFuel type: {self.fuel_type}\nRemaining fuel: {self.fuel_level}l'
    
    def add_fuel(self, fuel_quantity):
        self.fuel_level -= fuel_quantity

    def change_price(self, new_price):
        self.fuel_price = new_price

    def change_type(self, new_type):
        self.fuel_type = new_type

    def refill_pump(self):
        self.fuel_level = 100        


class Car:
    def __init__(self):
        self.fuel_consumption = 0.5
        self.fuel_level = 50

    def __str__(self):
        return f'Fuel consumption: {self.fuel_consumption}l/km\nFuel level: {self.fuel_level}\nFuel level: {self.fuel_level}'

    def drive(self, distance):
        print('Vrum vrum!')
        self.fuel_level -= distance * self.fuel_consumption
    
    def fill_tank(self, fuel_quantity):
        self.fuel_level += fuel_quantity
        pump.add_fuel(fuel_quantity)


pump = FuelPump('Gasoline', 2.50)
print(pump)

beetle = Car()
print(beetle)
beetle.drive(10)
print(beetle)
beetle.fill_tank(10)
print(beetle)
print(pump)
