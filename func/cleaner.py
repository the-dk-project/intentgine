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

def domain_url(url):
    url = url.replace('https://', '')
    url = url.replace('http://', '')
    url = url.replace('www-beta.', '')
    url = url.replace('www.', '')
    url = url.replace('www1.', '')
    url = url.replace('www2.', '')
    url = url.replace('www3.', '')
    url = url.replace('www4.', '')
    url = url.replace('www5.', '')
    url = url.replace('www6.', '')
    url = url.replace('www7.', '')
    url = url.replace('www8.', '')

    return url