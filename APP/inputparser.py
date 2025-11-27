##   PYTHON FILE HEADER #
##
##   File:         [inputparser.py]
##
##   Author(s):    ['Pedro H.F Matias']
##   Site(s):      ['https://github.com/phfmatias']
##   Email(s):     ['phfmatias@discente.ufg.br']
##   Credits:      ['Copyright © 2025 LEEDMOL. All rights reserved.']
##   Date:         ['15.09.2025']
##   Version:      ['0.0.1']
##   Status:       ['Development']
##   Language:     ['Python']
##   Description:  ['Module to parse input parameters for the application']

from os import getcwd

class inputParser:
    def __init__(self):
        self.pwd = getcwd()
        self.qmprog = 'g16'
        self.ncores = 1
        self.mem = 8
        self.basis = 'jun-cc-pvdz' 
        self.functional = 'lc-blyp' 
        self.multiplicity = 1      
        self.charge = 0            
        self.parameter = 'jgap'    
        self.tolerance = 0.01      
        self.startOmega = 0.01
        self.endOmega =  1.00
        self.name = 'omega'
        self.aditonalKeywords = ''
        self.cPoints = False
        self.polarAxis = 'iso'
        self.system = 'Desktop'
        self.freq = [False, ]
        self.readCHK = None
        self.getParams()

    def getParams(self):
        try:
            params_file = open('omega.in', 'r')
        except:
            print("Error: Unable to open the input file 'omega.in'. Please ensure the file exists.")
            exit(0)

        for line in params_file.read().split('\n'):
            if 'polarAxis' in line.split():
                self.polarAxis = line.split()[2]
            if 'qmprog' in line.split():
                self.qmprog = line.split()[2]
            if 'parameter' in line.split():
                self.parameter = line.split()[2].lower()
            if 'ncores' in line.split():
                self.ncores = int(line.split()[2]) 
            if 'name' in line.split():
                self.name = line.split()[2]
            if 'basis' in line.split():
                self.basis = line.split()[2]
            if 'functional' in line.split():
                self.functional = line.split()[2]
            if 'chargeMolecule' in line.split():
                self.charge = int(line.split()[2])
            if 'multiplicity' in line.split():
                self.multiplicity = int(line.split()[2])
            if 'cPoints' in line.split():
                self.chargePoints = (line.split()[2] == 'True')
            if 'mem' in line.split():
                self.mem = int(line.split()[2])
            if 'aditonalKeywords' in line.split(' = '):
                self.aditonalKeywords = line.split(' = ')[1]
            if 'startOmega' in line.split():
                self.startOmega = float(line.split()[2])
            if 'endOmega' in line.split():
                self.endOmega = float(line.split()[2])
            if 'tolerance' in line.split():
                self.tolerance = float(line.split()[2])
            if 'freq' in line.split():
                self.freq = [True, line.split()[-1]]
            if 'readCHK' in line.split():
                self.readCHK = line.split()[2]
  
        params_file.close()

if __name__ == "__main__":
    parser = inputParser()
    parser.getParams()
    print(vars(parser))

