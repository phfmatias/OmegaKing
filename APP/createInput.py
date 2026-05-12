##   PYTHON FILE HEADER #
##
##   File:         [createInput.py]
##
##   Author(s):    ['Pedro H.F Matias']
##   Site(s):      ['https://github.com/phfmatias']
##   Email(s):     ['phfmatias@discente.ufg.br']
##   Credits:      ['Copyright © 2025 LEEDMOL. All rights reserved.']
##   Date:         ['15.09.2025']
##   Version:      ['0.0.1']
##   Status:       ['Development']
##   Language:     ['Python']
##   Description:  ['Module to create input files for quantum chemistry software']

#        CI = createInput(self._filePath, self._inputFile, self._functionals, self._basis, self._addKeywords, self._cpu, self._mem, self._freq, self._readCHK)



class createInput(object):
    def __init__(self, path, inputFileNeutral, inputFileCation, inputFileAnion, functional, basis, addKeywords, cpu, mem, freq, readCHK):
        self._path = path
        self._inputFileNeutral = inputFileNeutral
        self._inputFileCation = inputFileCation
        self._inputFileAnion = inputFileAnion
        self._functional = functional
        self._basis = basis
        self._addKeywords = addKeywords
        self._cpu = cpu
        self._mem = mem
        self._freq = freq
        self._readCHK = readCHK

    def createGaussianInput(self, omega, moleculeNeutral, moleculeCation, moleculeAnion, target, filename):

        self.convertOmega2String(omega)

        files = []

        try:
            name = self._inputFileNeutral.split('.')[0]
        except:
            name = self._inputFileNeutral.split('.')[0]

        omega = self.omega
        nameW = self.nameW
        
        if target in ['polarizability', 'jgap', 'deltaip']:

            additionalKeywords = self._addKeywords + ' IOP(3/107={0}) IOP(3/108={0})'.format(omega) + (' polar' if target == 'polarizability' else '')

            states = {
                "neutral": {"charge": 0, "multiplicity": 1},
                "cation": {"charge": 1, "multiplicity": 2},
                "anion": {"charge": -1, "multiplicity": 2},
            }

            files = []
            if target in ['jgap', 'deltaip']:
                for state, params in states.items():
                    fname = "{}_w{}_{}.gjf".format(filename, nameW, state)
                    if state == "neutral":
                        molecule = moleculeNeutral
                    elif state == "cation":
                        molecule = moleculeCation
                    else:
                        molecule = moleculeAnion
                    molecule.toGJF(
                        fileName=fname,
                        method=self._functional,
                        basis=self._basis,
                        charge=params["charge"],
                        multiplicity=params["multiplicity"],
                        addKeywords=additionalKeywords,
                        mem=self._mem,
                        procs=self._cpu,
                    )
                    files.append(fname)
            else: 
                fname = "{}_w{}.gjf".format(filename, nameW)
                molecule.toGJF(
                    fileName=fname,
                    method=self._functional,
                    basis=self._basis,
                    charge=0,
                    multiplicity=1,
                    addKeywords=additionalKeywords,
                    mem=self._mem,
                    procs=self._cpu,
                )
                files.append(fname)
                
        molecule.setCharge(0)
        molecule.setMultiplicity(1)

        return files

    def convertOmega2String(self, omega):
        omega = round(omega, 2)

        self.omega = "".join(str(omega).split('.')).ljust(10,"0")
        self.nameW = str(omega).replace('.', '')


