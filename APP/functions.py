##   PYTHON FILE HEADER #
##
##   File:         [functions.py]
##
##   Author(s):    ['Pedro H.F Matias']
##   Site(s):      ['https://github.com/phfmatias']
##   Email(s):     ['phfmatias@discente.ufg.br']
##   Credits:      ['Copyright © 2025 LEEDMOL. All rights reserved.']
##   Date:         ['17.09.2025']
##   Version:      ['0.0.1']
##   Status:       ['Development']
##   Language:     ['Python']
##   Description:  ['Calculate the functions needed for the application']

try:
    from APP.outputHandler import *
except ModuleNotFoundError:
    from outputHandler import *
import csv

from numpy import sqrt, power
from os import listdir

class Process():
    def __init__(self, omega, files, target, csv_file, polarAxis):
        self._omega = omega

        # print("####### DEBUG #######")
        # print("Processing files: " + ', '.join(files) + " for target: " + target)
        # print("Output will be saved in: " + csv_file.name)
        # print("Omega: " + str(omega))
        # print("####### DEBUG #######")

        if target == 'jgap' or target == 'deltaip':
            self._neutral = files[0]
            self._cation = files[1]
            self._anion = files[2]
            self.runOH()
            self.IP()
            self.EA()

        else:
            self._neutral = files[0]
            self._cation = None
            self._anion = None

        self._target = target
        self.csv_file = csv_file

        if target == 'jgap':
            self.targetFunction = self.JGAP()
        elif target == 'polarizability':
            self.targetFunction = self.POLARIZABILITY(polarAxis)
    
    def runOH(self):
        self.EN_TOTAL_NEUTRAL = OutputHandler.getEnergies(self, self._neutral)
        self.EN_TOTAL_CATION = OutputHandler.getEnergies(self, self._cation)
        self.EN_TOTAL_ANION = OutputHandler.getEnergies(self, self._anion)
        self.HOMO_NEUTRAL = OutputHandler.getHOMO(self, self._neutral)
        self.HOMO_CATION = OutputHandler.getHOMO(self, self._cation)
        self.HOMO_ANION = OutputHandler.getHOMO(self, self._anion)
        self.LUMO_NEUTRAL = OutputHandler.getLUMO(self, self._neutral)
        self.LUMO_CATION = OutputHandler.getLUMO(self, self._cation)
        self.LUMO_ANION = OutputHandler.getLUMO(self, self._anion)

    def IP(self):
        self.ip = self.EN_TOTAL_CATION - self.EN_TOTAL_NEUTRAL

    def EA(self):
        self.ea = self.EN_TOTAL_NEUTRAL - self.EN_TOTAL_ANION

    def JIP(self):
        self.jip = self.HOMO_NEUTRAL + self.ip

    def JEA(self):
        self.jea = self.HOMO_ANION + self.ea
    
    def JGAP(self):
        self.JIP()
        self.JEA()
        self.jgap = sqrt(power(self.jip, 2) + power(self.jea, 2))

        self.csv_file.write('{:.2f}, {:.8f}, {:.8f}, {:.8f}, {:.8f}, {:.8f}, {:.8f}, {:.8f}, {:.8f}, {:.8f}, {:.8f}, {:.8f}, {:.8f}, {:.8f}, {:.8f}\n'.format(self._omega, self.jgap, self.jip, self.jea, self.EN_TOTAL_CATION, self.EN_TOTAL_ANION, self.EN_TOTAL_NEUTRAL, self.HOMO_NEUTRAL, self.HOMO_ANION, self.HOMO_CATION, self.LUMO_NEUTRAL, self.LUMO_ANION, self.LUMO_CATION, self.ip, self.ea))

        return self.jgap

    def POLARIZABILITY(self, axis):
        self.polarizability = OutputHandler.getPolarizability(self, self._neutral, axis)
        self.csv_file.write('{:.8f}, {:.8f}\n'.format(self._omega, self.polarizability))

        return self.polarizability
    
if __name__ == "__main__":
    csvfile = open('Teste.csv','w')

    omegas = {0.62: '062', 0.39: '039', 0.24: '024', 0.16: '016', 0.10: '01'}

    for i in omegas:
        neutro = 'pna_neutro_w'+omegas[i]+'_neutral.log'
        cation = 'pna_neutro_w'+omegas[i]+'_cation.log'
        anion = 'pna_neutro_w'+omegas[i]+'_anion.log'

        print('Running for: ' + str(i))

        x = Process(i, [neutro, cation, anion], 'jgap', csvfile, 'xx')