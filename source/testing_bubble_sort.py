from sort_algorithms_22_1 import bubble_sort
from compare_functions import cmpr, my_cmpr

def sort_test(sort_function):
    data1 = [1, 2, 3, 4, 5]
    sorted_data1 = [1, 2, 3, 4, 5]
    data2 = [5, 4, 3, 2, 1]
    sorted_data2 = [1, 2, 3, 4, 5]
    data3 = [3, 2, 5, 1, 4]
    sorted_data3 = [1, 2, 3, 4, 5]
    data4 = [1]
    sorted_data4 = [1]
    data5 = []
    sorted_data5 = []
    data6 = [1, 2, 3, 1, 5]
    sorted_data6 = [1, 1, 2, 3, 5, ]
    data7 = [i for i in range(101)]
    sorted_data7 = data7.copy()
    e = data7.pop()
    data7.insert(0, e)
    data8 = [i for i in range(101)]
    sorted_data8 = data8.copy()
    d = data8.pop(0)
    data8.append(d)
    data = [data1, data2, data3, data4, data5, data6, data7, data8]
    sorted_data = [sorted_data1, sorted_data2, sorted_data3,
                   sorted_data4, sorted_data5, sorted_data6, sorted_data7,
                   sorted_data8]
    print("Testing of ", sort_function.__name__)

    wrong_counter = 0
    for i in range(len(data)):
        print("test", i, end=" ")
        compare_counter = sort_function(data[i],my_cmpr)  # sort_function --> bubble_sort(data[i])
        # Hier läuft er die ganze bubble Funktion durch
        if data[i] == sorted_data[i]:  # Vergleichen der sortierten Daten.
            print(f"O.K.(n = {len(data[i])},compares number = {compare_counter})")

        else:
            print("False")
            print("       Is  :", data[i])
            print("       Must:", sorted_data[i])
            wrong_counter += 1

    print("Wrong tests:", wrong_counter)

sort_test(bubble_sort)