def rec(m, l = 0):              # Рекурсивная функция. В нее передается массив из тела программы. Второй параметр l по умолчанию равен 0
                                # в дальнейшем в этот параметр будет передаваться индекс элемента, который надо выводить на печать
    if l >= len(m):
        print("Конец списка")
        return

    print(m[l])                 # на первой итерации печатаем m[0], затем индекс увеличиваем на 1 и передаем его снова в функцию, и так далее
    l += 1
    rec(m, l)


my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
rec(my_list)