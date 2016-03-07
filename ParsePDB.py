__description__ = ''' '''
__author__ = '''Guilhem Faure, PhD '''

dssp_exe = 'dsspcmbi'
from Bio.PDB import *
import sys


if __name__ == '__main__':
    parser_pdb = PDBParser()
    #parser_cif = MMCIFParser()

    try:
        p_pdb = sys.argv[1]
    except:
        raise('Provide a pdb file: python ParsePDB.pdb 1a2k.pdb')

    Mypdb = parser_pdb.get_structure('mystructure', p_pdb)
    #structure = Mypdb[0]


    #DSSP(structure, sys.argv[1])

    # This print Res Number XYZ bfactor
    for model in Mypdb:
        for chain in model:
            for residue in chain:
                res_name = residue.get_resname()
                ca_coord = list(residue['CA'].get_coord()) if residue.has_id('CA') else [None]*3
                bfactor = residue['CA'].get_bfactor() if residue.has_id('CA') else None
                res_nb = residue.get_id()

                print ('{res}\t{nb}\t{coords}\t{bfactor}'.
                       format(res       = res_name,
                              nb        = res_nb[1],
                              coords    = ' '.join(map(str, ca_coord)),
                              bfactor   = bfactor)
                       )