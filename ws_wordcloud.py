from func.reader import file_to_dict, pdf_reader, convert_pdf_to_txt, pdf_info
from func.cleaner import remove_excluded_words, remove_special_character
from func.compute import filter_word_count, string_counter
from func.file import pdf_report
from func import gdrive
from func import file
import os

def word_count(directory_id, output_path, elements):
    cwd = os.getcwd()
    special_characters = cwd + "\\conf\\special_chars.txt"
    excluded_words = cwd + "\\conf\\excluded_words.txt"
 
    titles = gdrive.dl_dir_files(directory_id)
    for title in titles:
        info = pdf_info(title)
        file.check_file(title)
        file.check_file(special_characters)
        file.check_file(excluded_words)
        input_string = convert_pdf_to_txt(title)
        sc_dict = file_to_dict(special_characters, " ")
        ew_dict = file_to_dict(excluded_words, " ")
        output_string = remove_special_character(input_string, sc_dict)
        output_string = remove_excluded_words(output_string, ew_dict)
        word_dict = string_counter(output_string, elements)
        results = filter_word_count(word_dict)
        pdf_report(output_path, results, info, title)
        os.remove(title)

word_count('1Ub6DCJTIw0U5XGUEPChydn6bmKV8VCD_', 'C:\\Users\\donnv\\Desktop\\1 Keyword\\', 1)
