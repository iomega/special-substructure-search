# -*- coding: utf-8 -*-
"""
Created on Wed May 23 11:56:10 2018
Read smiles from self made GNPS database and creates a file with all
molfiles.
Command line: python3 create_molfile.py GNPSdatabase
@author: stokm006
"""
from __future__ import print_function
from sys import argv
from rdkit import Chem

def make_smile_list(input_file):
    """ takes all text from GNPSdatabase (result from GNPSparser.py) and
    returns a list with exclusively the SMILES
    
    input_file: GNPS database (from GNPSparser)
    """
    smiles_list = []
    all_lines = input_file.split('\n')
    for line in all_lines:
        if line.startswith('SMILES'):
            line = line.split(', ')
            for word in line:
                word = word.lstrip('[').rstrip(']').strip('\'')
                smiles_list += [word]
            smiles_list = smiles_list[1:]
    return smiles_list
    
def write_molfile(input_file_name, data_smiles):
    """ takes all smiles and writes a file with the molfile information.
    
    input_file_name: name of the file which will be created
    data_smiles: list with all SMILES created with make_smile_list()
    """        
    output_file = open(input_file_name, 'w')
    output_file.write('GNPS Molfiles')
    output_file.write('\n\n')

    x = 0
    y = 0
    for i in range(len(data_smiles)):
        try:
            molfile = Chem.MolFromSmiles(data_smiles[i])
            y += 1
            recognized_molfiles = Chem.MolToMolBlock(molfile)
            output_file.write('SMILE {}: '.format(i+1) + data_smiles[i])            
            output_file.write(recognized_molfiles)
            output_file.write('\n\n')
        except:
            output_file.write('Unrecognized SMILE {}: '.format(i+1) + data_smiles[i])
            output_file.write('\n')
            x += 1
    output_file.write('Total nr of SMILES: ' + str(y))
    output_file.write('\n')    
    output_file.write('Total nr of unrecognized SMILES: '+ str(x))
            
if __name__ == "__main__":
    with open(argv[1]) as file_object:
        input_file = file_object.read()
        data_smiles = make_smile_list(input_file)
        write_molfile("MolfileData", data_smiles)
        

        