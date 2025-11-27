##   PYTHON FILE HEADER #
##
##   File:         [runQM.py]
##
##   Author(s):    ['Pedro H.F Matias']
##   Site(s):      ['https://github.com/phfmatias']
##   Email(s):     ['phfmatias@discente.ufg.br']
##   Credits:      ['Copyright © 2025 LEEDMOL. All rights reserved.']
##   Date:         ['15.09.2025']
##   Version:      ['0.0.1']
##   Status:       ['Development']
##   Language:     ['Python']
##   Description:  ['Module to run the quantum mechanics software']

'''
if len(inputs_) > 3:
print ("Runing the files {}" .format(', '.join(inputs_[0:3])))
popen_list = []
for inp in inputs_[0:3]:
    popen_list.append(popen("{} {}.gjf {}.log".format(self.__gaussian, self.__path + '/' + inp, self.__path + '/' + inp) , 'r'))
for p in popen_list:
    p.read()
popen_list = []
print ("Runing the files {}" .format(', '.join(inputs_[3:])))
for inp in inputs_[3:]:
    popen_list.append(popen("{} {}.gjf {}.log".format(self.__gaussian, self.__path + '/' + inp, self.__path + '/' + inp) , 'r'))
for p in popen_list:
    p.read()

'''

from os import popen
from time import time

class runQM():
    def __init__(self, files, header):
        self._header = header
        self._files = files

    def runGaussian(self):
        
        if len(self._files) <= 3:
            
            start = time()
            popen_list = []
            for file in self._files:
                popen_list.append(popen('g16 {}'.format(file), 'r'))
            for p in popen_list:
                p.read()
            end = start - time()
            self._header.write('Files {} runned in {:.2f} seconds\n' .format(', '.join(self._files), abs(end)))

        else:
            start = time()
            popen_list = []
            for file in self._files[0:3]:
                popen_list.append(popen('g16 {}'.format(file), 'r'))
            for p in popen_list:
                p.read()
            end = start - time()
            self._header.write('Files {} runned in {:.2f} seconds\n' .format(', '.join(self._files[0:3]), abs(end)))
            
            start = time()
            popen_list = []
            for file in self._files[3:]:
                popen_list.append(popen('g16 {}'.format(file), 'r'))
            for p in popen_list:
                p.read()
            end = start - time()
            self._header.write('Files {} runned in {:.2f} seconds\n' .format(', '.join(self._files[3:]), abs(end)))

