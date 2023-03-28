def run_ex02():
    f = open("zadanie2.csv", "r")
    second_splited_csv = []
    f.readline()
    for index, line in enumerate(f):
        splited_csv = line.split(",", maxsplit=1)
        second_splited_csv.append([])
        second_splited_csv[index].append(int(splited_csv[0]))
        second_splited_csv[index].append(splited_csv[1])

    new_list = []
    for element in second_splited_csv:
        if "\n" not in element:
            new_list.append(element)

    sorted_list = sorted(new_list)

    repaired_indexes = {}
    repaired_indexes[sorted_list[0][0]] = sorted_list[0][1]
    for splited_pair in sorted_list:
        if splited_pair[0] in repaired_indexes.keys():
            new_index = splited_pair[0] + 1
            repaired_indexes[new_index] = splited_pair[1]
        else:
            index = splited_pair[0]
            repaired_indexes[index] = splited_pair[1]

    lower_chars = {key: value.lower() for key, value in repaired_indexes.items()}

    delated_prefix = {}
    for key, value in lower_chars.items():
        split_words = value.split()
        for word in split_words[:-2]:
            if len(word) >= 2 and (ord(word[0]) == (ord(word[1]) - 1)):
                delated_prefix[key] = word
                print(f"id {key}: {word}")




    f.close()
