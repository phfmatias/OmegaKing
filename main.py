##   PYTHON FILE HEADER #
##
##   File:         [main.py]
##
##   Author(s):    ['Pedro H.F Matias']
##   Site(s):      ['https://github.com/phfmatias']
##   Email(s):     ['phfmatias@discente.ufg.br']
##   Credits:      ['Copyright © 2025 LEEDMOL. All rights reserved.']
##   Date:         ['15.09.2025']
##   Version:      ['0.0.1']
##   Status:       ['Development']
##   Language:     ['Python']
##   Description:  ['Main file to run the application']
##   Usage:		   ['python3 main.py']

from time import time

from APP.header import *
from APP.inputparser import *
from APP.moderator import *
from APP.plotter import *
from os import listdir

if __name__ == "__main__":
    start = time()

    h = header()
    header = h.headerfile
    csv_file = h.csvfile

    parameters = inputParser()

    header.write('------------ PARAMETERS ------------\n')
    for i in vars(parameters):
        header.write('{}: {}\n'.format(i, vars(parameters)[i]))
    header.write('------------ CALCULATIONS -------------\n')
    
    M = Moderator(parameters.pwd, parameters.name,parameters.functional, parameters.basis, parameters.aditonalKeywords, parameters.charge, parameters.multiplicity,parameters.ncores, parameters.mem,parameters.tolerance, parameters.startOmega, parameters.endOmega, parameters.qmprog, header, parameters.freq, parameters.readCHK, parameters.parameter, header, csv_file, parameters.polarAxis)

    header.write('---------------------------------------\n')

    csv_file.close()

    Plotter(parameters.name, parameters.parameter, parameters.polarAxis)

    end = start - time()

    header.write('Total time: {:.2f} seconds\n' .format(abs(end)))
    