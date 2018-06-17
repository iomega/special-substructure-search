# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 11:59:40 2018
Parses all data from original NuBBE CLASS database and writes a new uniform 
nubbe CLASS database and returns and writes a dictionary with all data.
Command line: python3 nubbe_parser.py nubbeCLASStry.txt
Command line: python3 nubbe_parser.py nubbeCLASS.txt
@author: stokm006
"""


from sys import argv

def parse_file(input_file):
    """ takes all text from nubbe database file and returns a list of lists 
    with NPs which is easy to use
    
    input_file: nubbe database txt file
    """
   
    all_lines = input_file.split('\n')
    all_info_list = []
    for line in all_lines:
        line = line.split('\t')
        info_per_row_list = []
        for value in line:
            my_string = ""
            if len(value) == 0:
                value = "NA"
            my_string += value
            info_per_row_list += [my_string]
        all_info_list += [info_per_row_list]
    return all_info_list
    
def write_CLASS_txtfile(input_file_name, data):
    """ takes all text from nubbe list and writes an 'uniform' nubbe CLASS 
    database.
    
    input_file_name: name of txt file that will be created
    data: nubbe list created with parse_file()
    """
    output_file = open(input_file_name, 'w')
    output_file.write('NuBBe CLASS database')
    output_file.write('\n\n')

    for line in data:
          output_file.write(str(line) +'\n')

      
def make_dict(data_for_dict):
    """ takes all text from nubbe list and makes a dictionary.
    
    data_for_dict: nubbe list created with parse_file()
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
    nubbe_dict = {}
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
             
        nubbe_dict[column_name_list[0]] = column_list1
        nubbe_dict[column_name_list[1]] = column_list2
        nubbe_dict[column_name_list[2]] = column_list3
        nubbe_dict[column_name_list[3]] = column_list4
        nubbe_dict[column_name_list[4]] = column_list5
        nubbe_dict[column_name_list[5]] = column_list6
        nubbe_dict[column_name_list[6]] = column_list7
        nubbe_dict[column_name_list[7]] = column_list8
        nubbe_dict[column_name_list[8]] = column_list9
        nubbe_dict[column_name_list[9]] = column_list10
        nubbe_dict[column_name_list[10]] = column_list11
    return (nubbe_dict)

def write_dict_txtfile(input_file_name, data_dict):
    """ takes all text from nubbe dictionary and writes it in a text file. 
    
    input_file_name: name of txt file that will be created
    data_dict: nubbe dictionary created with make_dict()
    """
  
    output_file = open(input_file_name, 'w')
    output_file.write('NuBBE database')
    output_file.write('\n\n')

    for  keys, values in data_dict.items():
        output_file.write(str(keys)+', '+str(values)+'\n')
                  
    
if __name__ == "__main__":
    with open(argv[1]) as file_object:
        input_file = file_object.read()
        parsed_data = parse_file(input_file)
        write_CLASS_txtfile("nubbe_CLASS_database", parsed_data)
        my_dictionary = make_dict(parsed_data)
        write_dict_txtfile("nubbe_database", my_dictionary)
