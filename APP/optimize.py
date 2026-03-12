##   PYTHON FILE HEADER #
##
##   File:         [control.py]
##
##   Author(s):    ['Pedro H.F Matias']
##   Site(s):      ['https://github.com/phfmatias']
##   Email(s):     ['phfmatias@discente.ufg.br']
##   Credits:      ['Copyright © 2025 LEEDMOL. All rights reserved.']
##   Date:         ['15.09.2025']
##   Version:      ['0.0.1']
##   Status:       ['Development']
##   Language:     ['Python']
##   Description:  ['Control module for the application']

from APP.goldenCalculator import *
from APP.createInput import *
from APP.runQM import *
from APP.functions import *
from APP.header import *
from time import time
from os import listdir

class Optimizer():
    def __init__(self, filePath, inputFileNeutral, inputFileCation, inputFileAnion, functionals, basis, addKeywords, charge, multiplicity, cpu, mem, tolerance, startOmega, endOmega, qmprog, arq, freq, readCHK, MK_MoleculeNeutral, MK_MoleculeCation, MK_MoleculeAnion, target, header, csv_file, polarAxis):
        
        self._filePath = filePath
        self._inputFileNeutral = inputFileNeutral
        self._inputFileCation = inputFileCation
        self._inputFileAnion = inputFileAnion
        self._functionals = functionals
        self._basis = basis
        self._addKeywords = addKeywords
        self._charge = charge
        self._multiplicity = multiplicity
        self._cpu = cpu
        self._mem = mem
        self._tolerance = tolerance
        self._startOmega = startOmega
        self._endOmega = endOmega
        self._qmprog = qmprog
        self._header = arq
        self._freq = freq
        self._readCHK = readCHK
        self.MK_MoleculeNeutral = MK_MoleculeNeutral
        self.MK_MoleculeCation = MK_MoleculeCation
        self.MK_MoleculeAnion = MK_MoleculeAnion
        self.target = target
        self._header = header
        self._csvfile = csv_file
        self._polarAxis = polarAxis

    def optimize(self):

        convergence = False

        omega_values = []
    
        GC = GoldenCalculator(self._startOmega, self._endOmega, self._tolerance)
        x1, x2 = GC.firstValues()

        omega_values.append(x1)
        omega_values.append(x2)

        CI = createInput(self._filePath, self._inputFileNeutral, self._inputFileCation, self._inputFileAnion, self._functionals, self._basis, self._addKeywords, self._cpu, self._mem, self._freq, self._readCHK)

        files_x1 = CI.createGaussianInput(x1, self.MK_MoleculeNeutral, self.MK_MoleculeCation, self.MK_MoleculeAnion, self.target)
        files_x2 = CI.createGaussianInput(x2, self.MK_MoleculeNeutral, self.MK_MoleculeCation, self.MK_MoleculeAnion, self.target)

        files = files_x1 + files_x2

        if self.target == 'jgap':
            self._csvfile.write('omega,ip,ea,jip,jea,jgap\n')
        elif self.target == 'polarizability':
            self._csvfile.write('omega,polarizability({})\n'.format(self._polarAxis))
        elif self.target == 'deltaip':
            self._csvfile.write('omega,ip,jip,deltaip\n')

        runQM(files,self._header).runGaussian()

        fx1 = Process(x1, files_x1, self.target, self._csvfile, self._polarAxis).targetFunction
        fx2 = Process(x2, files_x2, self.target, self._csvfile, self._polarAxis).targetFunction

        convergence, x1, x2 = GC.convergence(fx1, fx2)

        while not convergence:

            RQM = []
            
            if x1 in omega_values:
                sufix = '_w{}'.format(str(x1).replace('.', ''))
                files_x1 = [x for x in listdir() if sufix in x and '.log' in x]
                try:
                    order = {"neutral": 0, "cation": 1, "anion": 2}
                    files_x1.sort(key=lambda x: order[[key for key in order if key in x][0]])
                except:
                    pass
            
            elif x1 not in omega_values:
                files_x1 = CI.createGaussianInput(x1, self.MK_Molecule, self.target)
                RQM.extend(files_x1)
                omega_values.append(x1)

            if x2 in omega_values:
                sufix = '_w{}'.format(str(x2).replace('.', ''))
                files_x2 = [x for x in listdir() if sufix in x and '.log' in x]
                try:
                    order = {"neutral": 0, "cation": 1, "anion": 2}
                    files_x2.sort(key=lambda x: order[[key for key in order if key in x][0]])
                except:
                    pass

            elif x2 not in omega_values:
                files_x2 = CI.createGaussianInput(x2, self.MK_Molecule, self.target)
                RQM.extend(files_x2)
                omega_values.append(x2)
            
            if len(RQM) != 0:
                runQM(RQM,self._header).runGaussian()

            fx1 = Process(x1, files_x1, self.target, self._csvfile, self._polarAxis).targetFunction
            fx2 = Process(x2, files_x2, self.target, self._csvfile, self._polarAxis).targetFunction

            convergence, x1, x2 = GC.convergence(fx1, fx2)
            
        self._header.write('\nOptimal omega found: {:.2f}\n' .format(x1))
        self._header.write('---------------------------------------')
