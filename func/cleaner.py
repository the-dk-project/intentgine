from datetime import datetime
def remove_special_character(input_string, sc_dict):
    sc_list = list(sc_dict.keys())

    try:
        def replace_sc(special_character, string):
            return string.replace(special_character, '')

        for sc in sc_list:
            input_string = replace_sc(sc, input_string)

    except Exception as e:
        print(datetime.now(), "ERROR: {0}".format(e))

    finally:
        return input_string


def remove_excluded_words(input_string, uw_dict):
    ew_list = list(uw_dict.keys())

    try:
        string = str(input_string).split()
        filter_string = [word for word in string if word.upper() not in ew_list]
        output_string = ' '.join(filter_string)

    except Exception as e:
        print(datetime.now(), "ERROR: {0}".format(e))

    finally:
        return output_string
