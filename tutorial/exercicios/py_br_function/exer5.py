#Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais:
#taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é 
#o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o 
#imposto sobre vendas.

cost = float(input('Preço do produto: '))
tax = float(input('Taxa de imposto: '))

def somaimposto(tax, cost):
    return (1 + tax/100)*cost

print('Preço final:', somaimposto(tax,cost))