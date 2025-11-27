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

from APP.outputHandler import *
from numpy import sqrt, power

class Process():
    def __init__(self, omega, files, target, csv_file, polarAxis):
        self._omega = omega

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
        self.HOMO_CATION = OutputHandler.getHOMO(self, self._cation)[0]
        self.HOMO_ANION = OutputHandler.getHOMO(self, self._anion)[0]
        self.LUMO_NEUTRAL = OutputHandler.getLUMO(self, self._neutral)

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

        self.csv_file.write('{:.8f}, {:.8f}, {:.8f}, {:.8f}, {:.8f}, {:.8f}\n'.format(self._omega, self.ip, self.ea, self.jip, self.jea, self.jgap))

        return self.jgap

    def POLARIZABILITY(self, axis):
        self.polarizability = OutputHandler.getPolarizability(self, self._neutral, axis)
        self.csv_file.write('{:.8f}, {:.8f}\n'.format(self._omega, self.polarizability))

        return self.polarizability