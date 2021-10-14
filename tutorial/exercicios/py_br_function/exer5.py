#Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais:
#taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é 
#o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o 
#imposto sobre vendas.

cost = float(input('Preço do produto: '))
tax = float(input('Taxa de imposto: '))

def somaimposto(tax, cost):
    price = (1 + tax/100)*cost
    limited_float = round(price, 2)
    return limited_float

print('Preço final:', somaimposto(tax,cost))