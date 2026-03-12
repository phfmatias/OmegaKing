##   PYTHON FILE HEADER #
##
##   File:         [createMK_Molecule.py]
##
##   Author(s):    ['Pedro H.F Matias']
##   Site(s):      ['https://github.com/phfmatias']
##   Email(s):     ['phfmatias@discente.ufg.br']
##   Credits:      ['Copyright © 2025 LEEDMOL. All rights reserved.']
##   Date:         ['15.09.2025']
##   Version:      ['0.0.1']
##   Status:       ['Development']
##   Language:     ['Python']
##   Description:  ['Module to create a MoleKing Molecule from input file']

from MoleKing import Molecule, G16LOGfile
from os import listdir

class createMK_Molecule:
    def __init__(self, path, file):
        self._path = path
        self._file = file
        self.MK_Molecule = None
        self.createMK_Mol(file)

    def createMK_Mol(self, file):
        if '.' not in file:
            extension = ['.'+x.split('.')[-1] for x in listdir(self._path) if file == x.split('.')[0] and '.' in x][0]
            file = file+extension
        else:
            extension = '.'+file.split('.')[-1]

        if extension == '.gjf' or extension == '.com':
            mol = Molecule()
            arq = open(self._path + '/' + file, 'r').readlines()
            states = ['0 1\n', '1 2\n', '-1 2\n']
            for line in arq:
                if line in states:
                    start = arq.index(line) + 1
                    break
            for line in arq[start:]:
                if line == '\n':
                    end = arq.index(line, start)

            for line in arq[start:end]:
                try:
                    element = line.split()[0]
                    x = float(line.split()[1])
                    y = float(line.split()[2])
                    z = float(line.split()[3])
                    mol.addAtom(element, x, y, z)
                except:
                    pass

            for line in arq[end:]:
                try:
                    xq = float(line.split()[0])
                    yq = float(line.split()[1])
                    zq = float(line.split()[2])
                    qq = float(line.split()[3])
                    mol.addChargePoints(xq, yq, zq, qq)
                except:
                    pass
            
            if len(mol) == 0:
                print("Error: No atoms found in the {} file. Please check the file format or contact support.".format(extension))
                exit(0)
            
        elif extension == '.log':
            mol = G16LOGfile(self._path + '/' + file).getMolecule()
            if len(mol) == 0:
                print("Error: No atoms found in the log file. Please check if the calculation was completed successfully or contact support.")
                exit(0)

        elif extension == '.xyz':
            mol = Molecule()
            arq = open(self._path + '/' + file, 'r').readlines()[2:]
            for line in arq:
                try:
                    element = line.split()[0]
                    x = float(line.split()[1])
                    y = float(line.split()[2])
                    z = float(line.split()[3])
                    mol.addAtom(element, x, y, z)
                except:
                    pass
            if len(mol) == 0:
                print("Error: No atoms found in the xyz file. Please check the file format or contact support.")
                exit(0)
            
        else:
            print("Error: Unsupported file format. Please provide a .gjf, .com, .log, or .xyz file.")
            exit(0)

        self.MK_Molecule = mol
