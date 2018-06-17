# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 14:11:27 2018
Takes all data from original Streptomedb2 database and returns a structured 
dictionary with all data. This script also writes a self made Streptomedb 
database.
Werkt nog niet voor hele database bij line 66
Command line: python3 streptomedb_parser.py streptomedb-2try.sdf
Command line: python3 streptomedb_parser.py streptomedb-2.sdf
@author: stokm006
"""

from sys import argv

def make_dict(input_file):
    """ takes all text from streptomedb file and returns a list of lists with
    NPs which is easy to use
    
    input_file: streptomedb sdf file
    """
    
    my_string = ""
    all_lines = input_file.split('\n')
    for lines in all_lines:
        if not lines.startswith ('$$$$'):
            my_string += lines.strip('\n')
        if lines.startswith ('$$$$'):
            my_string += ('|')
    my_string = my_string.split('|')
    my_string = my_string[:-1]

    column_name_list = ['canonical_smiles', 'name', 'compound_id', 'molwt', \
    'HBD', 'HBA', 'rotatable bonds', 'pubchem cid', 'organism', 'pmids', \
    'activititis', 'synthesizing routes']
    
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
    column_list12 = []
    
    strep_dict = {}
    all_info_list = []
    for line in my_string:
        line = line.split('END>')
        line = line[1].split('>')
        my_list = []   
        for value in line:
            my_string = ""
            value = value.strip('\'"')
            if len(value) == 0:
                value = "NA"
            my_string += value
            my_list += [my_string]
        all_info_list += [my_list]
    

    for lists in all_info_list:    
        column_list1 += [lists[1]]        
        column_list2 += [lists[3]]
        column_list3 += [lists[5]]
        column_list4 += [lists[7]]        
        column_list5 += [lists[9]]
        column_list6 += [lists[11]]
        column_list7 += [lists[13]]        
        column_list8 += [lists[15]]
        column_list9 += [lists[17]]
        column_list10 += [lists[19]]
        column_list11 += [lists[21]]
        column_list12 += [lists[23]]

    strep_dict[column_name_list[0]] = column_list1
    strep_dict[column_name_list[1]] = column_list2
    strep_dict[column_name_list[2]] = column_list3
    strep_dict[column_name_list[3]] = column_list4
    strep_dict[column_name_list[4]] = column_list5
    strep_dict[column_name_list[5]] = column_list6
    strep_dict[column_name_list[6]] = column_list7
    strep_dict[column_name_list[7]] = column_list8
    strep_dict[column_name_list[8]] = column_list9
    strep_dict[column_name_list[9]] = column_list10
    strep_dict[column_name_list[10]] = column_list11
    strep_dict[column_name_list[11]] = column_list12
    return (strep_dict)

def write_dict_txtfile(input_file_name, data_dict):
    """ takes all text from streptomedb dictionary and writes it in a text file. 
    
    input_file_name: name of txt file that will be created
    data_dict: strep dictionary created with make_dict()
    """
    output_file = open(input_file_name, 'w')
    output_file.write('Streptomedb2 database')
    output_file.write('\n\n')

    for  keys, values in data_dict.items():
        output_file.write(str(keys)+', '+str(values)+'\n')


  
def parse_file(data_dict):
    """ takes the streptomedb dictionary and returns a list of lists with
    NPs which is easy to use
    
    data_dict: strep dictionary created with make_dict()
    """
    key_list = []
    for key in data_dict.keys():
        key_list += [key]
    
    value_list = []
    for value in data_dict.values():
        value_list += [value]

    value_list = [list(i) for i in zip(*value_list)]
    info_list = [key_list] + value_list
    
    return info_list
    

 
def write_list_txtfile(input_file_name, data):
    """ takes all text from streptomdb list and writes a database.
    
    input_file_name: name of txt file that will be created
    data: streptomdb list created with parse_file()
    """
    output_file = open(input_file_name, 'w')
    output_file.write('Streptomedb2 database')
    output_file.write('\n\n')

    for line in data:
          output_file.write(str(line) +'\n')
        
if __name__ == "__main__":
    with open(argv[1]) as file_object:
        input_file = file_object.read()
        my_dictionary = make_dict(input_file)
        write_dict_txtfile("streptome_database", my_dictionary)
        data = parse_file(my_dictionary)
        write_list_txtfile("streptome_list_database", data)

