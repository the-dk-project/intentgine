import statistics

def filter_word_count(dictionary):
    dict_values = [x for x in dictionary.values() if x != 1]
    median_value = statistics.median(dict_values)
    word_dict = dict()
    for key, value in dictionary.items():
        if value > median_value:
            word_dict[key] = value

    return word_dict


def word_count(input_string):
    words = input_string.split()

    word_dict = dict()

    for word in words:
        if word in word_dict.keys():
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    return word_dict

def string_counter(input_string, element):
    ctr = 0
    e = int(element)
    word_dict = dict()
    words = str(input_string).split(" ")

    for word in words:
        output_string = str(" ".join(words[ctr:ctr+e]))
        if ctr <= (len(words) - e):
            if output_string in word_dict.keys():
                word_dict[output_string] += 1
            else:
                word_dict[output_string] = 1
                word_dict[word] = 1
        ctr += 1

    return word_dict