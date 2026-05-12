##   PYTHON FILE HEADER #
##
##   File:         [moderator.py]
##
##   Author(s):    ['Pedro H.F Matias']
##   Site(s):      ['https://github.com/phfmatias']
##   Email(s):     ['phfmatias@discente.ufg.br']
##   Credits:      ['Copyright © 2025 LEEDMOL. All rights reserved.']
##   Date:         ['15.09.2025']
##   Version:      ['0.0.1']
##   Status:       ['Development']
##   Language:     ['Python']
##   Description:  ['Module to moderate the simulation process']

from APP.createMK_Molecule import *
from APP.optimize import *

class Moderator(object):
    def __init__(self, path, inputFileNeutral, inputFileCation, inputFileAnion, functionals, basis, addKeywords, charge, multiplicity, cpu, mem, tolerance, startOmega, endOmega, qmprog, arq, freq, readCHK, target, header, csv_file, polarAxis, filename):
        
        self._path = path
        self._inputfileNeutral = inputFileNeutral
        self._inputfileCation = inputFileCation
        self._inputfileAnion = inputFileAnion
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
        self.target = target
        self._header = header
        self._csvfile = csv_file
        self._polarAxis = polarAxis
        self._filename = filename
        self.MK_MoleculeNeutral = createMK_Molecule(self._path, self._inputfileNeutral).MK_Molecule
        self.MK_MoleculeCation = createMK_Molecule(self._path, self._inputfileCation).MK_Molecule
        self.MK_MoleculeAnion = createMK_Molecule(self._path, self._inputfileAnion).MK_Molecule
        self.OptimizeFunctional()

    def OptimizeFunctional(self):

        x = Optimizer(self._path, self._inputfileNeutral, self._inputfileCation, self._inputfileAnion, self._functionals, self._basis, self._addKeywords, self._charge, self._multiplicity, self._cpu, self._mem, self._tolerance, self._startOmega, self._endOmega, self._qmprog, self._header, self._freq, self._readCHK, self.MK_MoleculeNeutral, self.MK_MoleculeCation, self.MK_MoleculeAnion, self.target, self._header, self._csvfile, self._polarAxis, self._filename)

        x.optimize()


