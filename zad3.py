import time


def open_and_validate_file():
    with open('SJP.txt', 'r', encoding='utf-8') as sjp:
        # wolne list comp
        s_time1 = time.time()
        sjp_text = [word[:-2] for word in sjp]
        time1 = time.time() - s_time1
        print(f'Czas wykonania list comp: {time1} s')

        # szybsze wykonanie w pętli
        sjp_text1 = []
        s_time2 = time.time()
        for word in sjp:
            sjp_text1.append(word[:-2])
        time2 = time.time() - s_time2
        print(f'Czas wykonania w zwykłej pętli: {time2}')
    return sjp_text


def input_data():
    input_text = input("Wpisz przykładowy tekst: ").lower()
    while len(input_text.split()) != 1:
        input_text = input("Wpisz przykładowy tekst: ").lower()
    return input_text


def linear_search(sjp_text):
    input_text = input_data()
    # Wyszukiwanie liniowe
    s_time = time.time()
    while True:
        if input_text == '1':
            break
        if input_text in sjp_text:
            print(f'Wyraz {input_text} jest zgodny z SJP')
        else:
            print(f'Wyraz {input_text} nie występuje w SJP')
        print(f'Czas wykonania: {time.time() - s_time}')
    print('\nZakończenie programu\n')


def optimized_search_sjp(sjp_text):
    # mapowanie
    letters = [letter for letter in 'a, ą, b, c, ć, d, e, ę, f, g, h, i, j, k, l, ł, m, n, ń, o, ó, p, r, s, ś,' \
                                    ' t, u, w, y, z, ź, ż'.split(', ')]
    mapped_words = {}
    tmp_list = []
    remembered_index = 0
    for letter in letters:
        for index, word in enumerate(sjp_text[remembered_index:]):
            if word[0] != letter and remembered_index < index:
                remembered_index = index
                break
            if word[0] == letter:
                tmp_list.append(word)
        mapped_words[letter] = tmp_list
        tmp_list = []
    return mapped_words


def check_in_sjp(mapped_words, sjp_text):
    while True:
        input_text = input_data()
        if input_text == '1':
            break
        if input_text in mapped_words[input_text[0]]:
            s_time = time.time()
            if input_text in sjp_text:
                print(f'Wyraz {input_text} jest zgodny z SJP')
            else:
                print(f'Wyraz {input_text} nie występuje w SJP')
            print(f'Czas wyszukiwania: {time.time() - s_time}')
    print('\nZakończenie programu\n')


def run_prog():
    sjp_text = open_and_validate_file()
    mapped_words = optimized_search_sjp(sjp_text)

    check_in_sjp(mapped_words, sjp_text)

    # linear_search(sjp_text)






