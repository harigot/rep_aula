#Faça um programa para imprimir:
#    1
#    2   2
#    3   3   3
#    .....
#    n   n   n   n   n   n  ... n

def output_nth(num = 5):
    num += 1
    for j in range(1, num):
        list = []
        for i in range(1, j + 1):
            list.append(j)
        print(list)

num = int(input('number: '))
output_nth(num)
