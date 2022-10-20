array = input("Введите последовательность чисел через пробел: ").split()
array = [int(x) for x in array]
element = int(input("Введите элемент, для поиска в последовательности выше. \n"
                    "Любую цифру или число:"))

for i in range(len(array)):
    for j in range(len(array)-i-1):
        if array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]

def binary_search(array, element, left, right):
    if left > right:
        return False

    middle = (right + left) // 2

    if array[middle] == element:
        return middle -1, middle
    elif array[left] == array[right]:
        if element < array[middle]:
            return middle - 1,middle
        else:
            return middle, middle + 1
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)

print(f'Отсортированный список, вашей последовательности чисел:{array}')
if element <= array[0] or element >= array[-1]:
    print("Введенный элемент не соответствует условиям задачи, полиция уже выехала!")
else:
    print(f'Первый индекс, цифры или числа, стоящего перед введенным элементом. \n'
          f'Второй индекс самого элемента или стоящего за ним \n'
          f'{binary_search(array, element, 0, len(array)-1)}')