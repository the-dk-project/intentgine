from func.reader import file_to_dict, pdf_reader, convert_pdf_to_txt, pdf_info
from func.cleaner import remove_excluded_words, remove_special_character
from func.compute import filter_word_count, string_counter
from func.file import pdf_report
from func import gdrive
from func import file
import os

def word_count(directory_id, input_file, output_file, elements):
    cwd = os.getcwd()
    #if output_file:
    #    os.remove(output_file)
    special_characters = cwd + "\\conf\\special_chars.txt"
    excluded_words = cwd + "\\conf\\excluded_words.txt"

    gdrive.dl_file_name(directory_id, input_file)
    info = pdf_info(input_file)
    file.check_file(input_file)
    file.check_file(special_characters)
    file.check_file(excluded_words)
    input_string = convert_pdf_to_txt(input_file)
    sc_dict = file_to_dict(special_characters, " ")
    ew_dict = file_to_dict(excluded_words, " ")
    output_string = remove_special_character(input_string, sc_dict)
    output_string = remove_excluded_words(output_string, ew_dict)
    word_dict = string_counter(output_string, elements)
    results = filter_word_count(word_dict)
    pdf_report(output_file, results, info)
    os.remove(input_file)

word_count('1fXEDtthQmVyqjNAOus1qw3jDgu4ve4vb', '61017_ScalingDataIntegrationtoHandle.PDF', 'C:\\Users\\donnv\\Desktop\\result.xlsx', 2)
