##   PYTHON FILE HEADER #
##
##   File:         [outputHandler.py]
##
##   Author(s):    ['Pedro H.F Matias']
##   Site(s):      ['https://github.com/phfmatias']
##   Email(s):     ['phfmatias@discente.ufg.br']
##   Credits:      ['Copyright © 2025 LEEDMOL. All rights reserved.']
##   Date:         ['17.09.2025']
##   Version:      ['0.0.1']
##   Status:       ['Development']
##   Language:     ['Python']
##   Description:  ['Output handler module for the application']

from MoleKing import G16LOGfile

class OutputHandler():
    def __init__(self):
        pass

    def getEnergies(self, file):
        file = file.replace('.gjf', '.log')
        mol = G16LOGfile(file)
        return mol.getEnergy()
    
    def getHOMO(self, file):
        file = file.replace('.gjf', '.log')
        mol = G16LOGfile(file)

        homo = mol.getHOMO()
        if isinstance(homo, (list, tuple)):
            return homo[0]
        return homo
        
    def getLUMO(self, file):
        file = file.replace('.gjf', '.log')
        mol = G16LOGfile(file)
        lumo = mol.getLUMO()
        if isinstance(lumo, (list, tuple)):
            return lumo[0]
        return mol.getLUMO()
    
    def getPolarizability(self, file, axis):  
        file = file.replace('.gjf', '.log')
        mol = G16LOGfile(file, polarAsw=True)
        
        return mol.getAlpha(axis)[axis]