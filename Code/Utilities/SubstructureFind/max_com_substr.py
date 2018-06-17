# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 11:58:36 2018
Maximum Common Substructures
Command line: python3 max_com_substr.py
@author: stokm006
"""
from __future__ import print_function
from rdkit import Chem
from rdkit.Chem import rdFMCS

def max_common_substructures():
    mol1 = Chem.MolFromSmiles("c1ccccc1O")
    mol2 = Chem.MolFromSmiles("c1ccccc1")
    mol3 = Chem.MolFromSmiles("c1ccccc1N")

    mols = [mol1,mol2,mol3]
    res=rdFMCS.FindMCS(mols)
    print (res.numAtoms)
    print (res.numBonds)
    print (res.smartsString)


if __name__ == '__main__':
    max_common_substructures()


