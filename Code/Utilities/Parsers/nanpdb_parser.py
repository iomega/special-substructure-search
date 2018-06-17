# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 10:59:20 2018
A Resource for Natural Products from Northern African Sources (nanpdb)
Parses all data from original nanp database (CLASS file not available) and 
writes a new uniform nanp database and returns and writes a dictionary with all 
data.
Command line: python3 nanpdb_parser.py nanpdbCLASStry.txt
Command line: python3 nanpdb_parser.py nanpdbCLASS.txt
@author: stokm006
"""


from sys import argv

def parse_file(input_file):
    """ takes all text from nanpdb database file and returns a list of lists 
    with NPs which is easy to use.
  
    input_file: nanpdb database txt file
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
    return (all_info_list)

    
def write_list_txtfile(input_file_name, data):
    """ takes all text from nanpdb list and writes a nanpdb database.
    
    input_file_name: name of txt file that will be created
    data: nanpdb list created with parse_file()
    """

    output_file = open(input_file_name, 'w')
    output_file.write('NANP database')
    output_file.write('\n\n')
    output_file.write(str(['Compound name', 'SMILES']))
    output_file.write('\n')

    for line in data:
        output_file.write("['"+str(line[2])+"', '" + str(line[0])+"']" +'\n')
  
   
def make_dict(data_for_dict):
    
    """ takes all text from nanpdb list and makes a dictionary.
    
    data_for_dict: nanpd list created with parse_file()
    """    
    column_name_list = ['Compound name', 'SMILES']
    db_list = data_for_dict
    
    column_list1 = []
    column_list2 = []
    nanpdb_dict = {}
    for line in db_list:
        my_string1 = '' 
        my_string2 = ''
        
        my_string1 = line[2]
        column_list1 += [my_string1]
        my_string2 = line[0]
        column_list2 += [my_string2]
        
        nanpdb_dict[column_name_list[0]] = column_list1
        nanpdb_dict[column_name_list[1]] = column_list2

    return (nanpdb_dict)

def write_dict_txtfile(input_file_name, data_dict):
    """ takes all text from nanpdb dictionary and writes it in a text file. 
    
    input_file_name: name of txt file that will be created
    data_dict: nanpdb dictionary created with make_dict()
    """
    
    output_file = open(input_file_name, 'w')
    output_file.write('NANP database')
    output_file.write('\n\n')

    for  keys, values in data_dict.items():
        output_file.write(str(keys)+', '+str(values)+'\n')


if __name__ == "__main__":
    with open(argv[1]) as file_object:
        input_file = file_object.read()
        parsed_data = parse_file(input_file)
        write_list_txtfile("nanpdb_list_database", parsed_data)
        my_dictionary = make_dict(parsed_data)
        write_dict_txtfile("nanpdb_database", my_dictionary)
