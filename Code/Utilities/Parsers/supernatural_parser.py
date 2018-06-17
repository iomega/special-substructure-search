# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 09:03:08 2018
Parses all data from original Super Natural (SN) database and and writes a new 
uniform SN CLASS database and returns and writes a dictionary with all data.
Command line: python3 supernatural_parser.py supernaturalCLASStry.txt
Command line: python3 supernatural_parser.py supernaturalCLASS.txt
@author: stokm006
"""
from sys import argv


def parse_file(input_file):
    """ takes all text from SN database file and returns a list of lists with
    NPs which is easy to use
    
    input_file: SN database txt file
    """
   
    all_lines = input_file.split('\n')
    all_info_list = []
    for line in all_lines:
        line = line.split('\t')
        info_per_row_list = []
        for value in line:
            my_string = ""
            value = value.strip('\'"')
            if len(value) == 0:
                value = "NA"
            my_string += value
            info_per_row_list += [my_string]
        all_info_list += [info_per_row_list]

    return all_info_list

def write_CLASS_txtfile(input_file_name, data):
    """ takes all text from SN list and writes an 'uniform' GNPS CLASS 
    database.
    
    input_file_name: name of txt file that will be created
    data: SN list created with parse_file()
    """
    output_file = open(input_file_name, 'w')
    output_file.write('Super Natural CLASS database')
    output_file.write('\n\n')

    for line in data:
          output_file.write(str(line) +'\n')

      
def make_dict(data_for_dict):
    """ takes all text from SN list and makes a dictionary.
    
    data_for_dict: SN list created with parse_file()
    """                
    
    column_name_list = data_for_dict[0]
    db_list = data_for_dict[1:]
         
    column_list1 = []
    column_list2 = []
    column_list3 = []
    column_list4 = []
    column_list5 = []
    column_list6 = []
    column_list7 = []
    column_list8 = []
    column_list9 = []
    column_list10 = []
    column_list11 = []
    SN_dict = {}
    for line in db_list:
        my_string1 = '' 
        my_string2 = ''
        my_string3 = ''
        my_string4 = ''
        my_string5 = ''
        my_string6 = ''
        my_string7 = ''
        my_string8 = ''
        my_string9 = ''
        my_string10 = ''
        my_string11 = ''

        my_string1 = line[0]
        column_list1 += [my_string1]
        my_string2 += line[1]
        column_list2 += [my_string2]
        my_string3 += line[2]
        column_list3 += [my_string3]
        my_string4 += line[3]
        column_list4 += [my_string4]
        my_string5 += line[4]
        column_list5 += [my_string5]
        my_string6 += line[5]
        column_list6 += [my_string6]
        my_string7 += line[6]
        column_list7 += [my_string7]
        my_string8 += line[7]
        column_list8 += [my_string8]
        my_string9 += line[8]
        column_list9 += [my_string9]
        my_string10 += line[9]
        column_list10 += [my_string10]
        my_string11 += line[10]
        column_list11 += [my_string11]         
             
        SN_dict[column_name_list[0]] = column_list1
        SN_dict[column_name_list[1]] = column_list2
        SN_dict[column_name_list[2]] = column_list3
        SN_dict[column_name_list[3]] = column_list4
        SN_dict[column_name_list[4]] = column_list5
        SN_dict[column_name_list[5]] = column_list6
        SN_dict[column_name_list[6]] = column_list7
        SN_dict[column_name_list[7]] = column_list8
        SN_dict[column_name_list[8]] = column_list9
        SN_dict[column_name_list[9]] = column_list10
        SN_dict[column_name_list[10]] = column_list11
    return (SN_dict)


def write_dict_txtfile(input_file_name, data_dict):
    """ takes all text from SN dictionary and writes it in a text file. 
    
    input_file_name: name of txt file that will be created
    data_dict: SN dictionary created with make_dict()
    """
    
    output_file = open(input_file_name, 'w')
    output_file.write('Super Natural database')
    output_file.write('\n\n')

    for  keys, values in data_dict.items():
        output_file.write(str(keys)+', '+str(values)+'\n')


if __name__ == "__main__":
    with open(argv[1]) as file_object:
        input_file = file_object.read()
        parsed_data = parse_file(input_file)
        write_CLASS_txtfile("supernatural_CLASS_database", parsed_data)
        my_dictionary = make_dict(parsed_data)
        write_dict_txtfile("supernatural_database", my_dictionary)

