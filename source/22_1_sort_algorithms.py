def bubble_sort(my_list):
    """
    Sort list bubble algo
    :param my_list:  list to be sorted and sorted list
    :return: None
    """
    first_unsorted = 0
    last_unsorted = len(my_list)-1
    compare_counter = 0
    while first_unsorted < last_unsorted:
        start_unsorted = last_unsorted
        finish_unsorted = first_unsorted
        step = -1
#        start_unsorted = first_unsorted # Für den Fall von links nach rechts
#        finish_unsorted = last_unsorted
#        step = 1
        new_finish_unsorted = start_unsorted
        for i in range(start_unsorted,finish_unsorted,step):
            compare_counter += 1
#            if my_list[i] > my_list[i + step]: # Für den Fall von links nach rechts
            if my_list[i] < my_list[i + step]:
                my_list[i], my_list[i + step] = my_list[i + step], my_list[i]  # Plätzetausch Pythonic way
                new_finish_unsorted = i
#        last_unsorted = new_finish_unsorted # Für den Fall von links nach rechts
        first_unsorted = new_finish_unsorted

    return compare_counter

# 18.1.2022 -- Bubble sort mit wechsel von iterations Richtung.  Q: was bring mir das?
# Dabei soll sich rechts und links ein sortierter Teil bilden. Die MItte bleibt unsortiert.

# First = 0 , last = len()-1
# Wie kann man sich nach einem Durchlauf merken welcher Teil der Soldaten sortiert ist?


## 2 Noch einen Algo: insertion algorithmus. --> Ich suche den größten und schiebe ihn nach ganz rechts.
## Der ganz rechts stand tauscht die Plätze mit dem größten.

# Richtung von der Sortierung wechseln zum optimieren.
# Feststellen welcher Teil der Liste bereits sortiert ist.

# 1. Effektivität visualisieren: (Ausführungszeit sichtbar machen)
# 2. Zwei test sets einführen: (100,0,1,2,...,99) (1,2,...,100,0)
# 2. Beide Sortierungs-Richtungen erlauben: (links-rechts, rechts-links)
# 3. Umsortierten Teil der Liste definieren.


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
        compare_counter = sort_function(data[i])  # sort_function --> bubble_sort(data[i])
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
