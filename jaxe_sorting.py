from tutorial.aulas.jaxe_classes.sorting.change_later import insertion_sort
from tutorial.exercicios.py_br_class.exer4 import Person



def sort_by_age(p_list):
    print(insertion_sort(p_list))
    # new_list = map(lambda p: p.age, p_list)
    # print(insertion_sort(list(new_list)))


p1 = Person('carlos', 61, 70, 2)
p2 = Person('carlota', 96, 70, 2)
p3 = Person('carl', 69, 70, 2)
p4 = Person('carlinhos', 48, 70, 2)

p_list = [p1, p2, p3, p4]

sort_by_age(p_list)

# newlist = sorted(p_list, key=lambda p: p.age, reverse=False)
# newlist = map(lambda p: str(p), newlist)
# print(list(newlist))

