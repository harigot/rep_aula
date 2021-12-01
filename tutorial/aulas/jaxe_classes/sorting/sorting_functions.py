#I made this functions to learn about sorting algorithms and to import 
#functions in other files properly.


from heapq import heappop, heapify


# def insertion_sort(array):
#     for i in range(1,len(array)):
#         j = i
#         while j > 0 and array[j] < array[j-1]:
#             array[j], array[j-1] = array[j-1], array[j]
#             j -= 1
#     return array


# def recursive_insertion_sort(array, i = 1):
#     value = array[i]
#     j = i
#     while j > 0 and array[j-1] > value:
#         array[j] = array[j-1]
#         j -= 1
#     array[j] = value
#     if i < len(array)-1:
#         recursive_insertion_sort(array, i+1)
#     return array
    

# def heap_sort(array):
#     heapify(array)
#     sorted = []
#     while array:
#         sorted.append(heappop(array))
#     return sorted


def block_sort(array, block_size):
    for i in range(0, len(array), block_size):
        insertion_sort(array[i:i+block_size])
    return array


mess = [6,2,7,3,5,1,2,6,7,8,5]
print(block_sort(mess, 5 ))