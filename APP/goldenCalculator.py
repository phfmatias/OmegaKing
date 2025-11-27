##   PYTHON FILE HEADER #
##
##   File:         [goldenCalculator.py]
##
##   Author(s):    ['Pedro H.F Matias']
##   Site(s):      ['https://github.com/phfmatias']
##   Email(s):     ['phfmatias@discente.ufg.br']
##   Credits:      ['Copyright © 2025 LEEDMOL. All rights reserved.']
##   Date:         ['15.09.2025']
##   Version:      ['0.0.1']
##   Status:       ['Development']
##   Language:     ['Python']
##   Description:  ['This module contains the GoldenCalculator class to calculate w1 and w2 parameters.']

from math import sqrt

class GoldenCalculator(object):
    def __init__(self, startValue, endValue, tolerance):
        self.x_a = startValue
        self.x_b = endValue
        self.tol = tolerance
        self.goldenRate = (sqrt(5) - 1) / 2

    def d(self, x_a, x_b):
        return self.goldenRate * (x_b - x_a)    
    
    def newX1(self, x_a, x_b):
        return x_a + self.d(x_a, x_b)
    
    def newX2(self, x_a, x_b): 
        return x_b - self.d(x_a, x_b)
    
    def firstValues(self):
        self.x1 = round(self.newX1(self.x_a, self.x_b), 2)
        self.x2 = round(self.newX2(self.x_a, self.x_b), 2)
        return self.x1, self.x2
    
    def convergence(self, f_x1, f_x2):
        if abs(self.x_a - self.x_b) < self.tol:
            if f_x1 > f_x2:
                final = self.x1
            else:
                final = self.x2
            return (True, round(final,2) , None)
        else:
            if f_x1 < f_x2:
                self.x_a = self.x2
                self.x2 = self.x1
                self.x1 = self.newX1(self.x_a, self.x_b)
            else:
                self.x_b = self.x1
                self.x1 = self.x2
                self.x2 = self.newX2(self.x_a, self.x_b)

            return (False, round(self.x1,2), round( self.x2,2))
