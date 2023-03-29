'''
For manual testing run:
py quick_sort.py
'''

from random import randrange

def quick_sort(collection: list[int]) -> list[int]:
    '''Python implementation of quick sort algorithm.
    
    Examples:
    >>[]
    []
    >>[-5,8,2,9,4]
    [-5,2,4,8,9]
    '''

    if len(collection) < 2:
        return collection
    
    pivot_index = randrange(len(collection)) # use random element as pivot
    pivot = collection[pivot_index]
    greater = [] # all elements greater than pivot
    lesser = [] # all elements lesser than pivot

    for element in collection[: pivot_index]:
        (greater if element > pivot else lesser).append(element)

    for element in collection[pivot_index + 1 :]:
        (greater if element > pivot else lesser).append(element)

    return quick_sort(lesser) + [pivot] + quick_sort(greater)

if __name__ == '__main__':
    # prompt = 'Enter numbers seperated by a comma\n>>'
    # user_input = input(prompt)
    # unsorted = [int(elem) for elem in user_input.split(',')]
    print(quick_sort([randrange(1000) for _ in range(200)]))