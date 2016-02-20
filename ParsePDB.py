__description__ = ''' '''
__author__ = '''Guilhem Faure, PhD '''

from Bio.PDB import *



if __name__ == '__main__':
    parser_pdb = PDBParser()
    parser_cif = MMCIFParser()


    Mypdb = parser_pdb.get_structure('mystructure', '1a2k.pdb')

    for model in Mypdb:
        for chain in model:
            for residue in chain:
                print (chain, residue)
                for atom in residue:
                    print (chain, residue, atom)
    pass