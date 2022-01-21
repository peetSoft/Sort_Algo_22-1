def bubble_sort(my_list, cmpr):
    """
    Sort list bubble algo
    :param my_list:  list to be sorted and sorted list
    :return: None
    """
    original_first_unsorted = 0
    original_last_unsorted = len(my_list) - 1
    compare_counter = 0
    from_left_to_right = False
    while original_first_unsorted < original_last_unsorted:
        from_left_to_right = not from_left_to_right
        if from_left_to_right:
            start_unsorted = original_first_unsorted  # Für den Fall von links nach rechts
            finish_unsorted = original_last_unsorted
            step = 1
        else:
            start_unsorted = original_last_unsorted
            finish_unsorted = original_first_unsorted
            step = -1
        new_finish_unsorted = start_unsorted
        for i in range(start_unsorted, finish_unsorted, step):
            compare_counter += 1
            if (from_left_to_right and cmpr(my_list[i], my_list[i + step]) > 0
                    or
                    not from_left_to_right and cmpr(my_list[i], my_list[i + step]) < 0):
                my_list[i], my_list[i + step] = my_list[i + step], my_list[i]  # Plätzetausch Pythonic way
                new_finish_unsorted = i
        if from_left_to_right:
            original_last_unsorted = new_finish_unsorted  # Für den Fall von links nach rechts
        else:
            original_first_unsorted = new_finish_unsorted

    return compare_counter

# 20.1.2022 Mögliche Verbesserung: Jetzt ist schlecht bubble_sort vergleicht nur Zahlen und kann diese nur
# aufsteigend sortieren
# --> Wir wollen: Sortierungskriterium frei definieren können
# --> Wie machen wir das? Dafür führen wir eine compare-Funktion ein. Diese compare_Funktion wird ein Parameter
# Für bubble_sort


## 2 Noch einen Algo: insertion algorithmus. --> Ich suche den größten und schiebe ihn nach ganz rechts.
## Der ganz rechts stand tauscht die Plätze mit dem größten.

