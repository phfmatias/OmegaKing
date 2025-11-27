##   PYTHON FILE HEADER #
##
##   File:         [plotter.py]
##
##   Author(s):    ['Pedro H.F Matias']
##   Site(s):      ['https://github.com/phfmatias']
##   Email(s):     ['phfmatias@discente.ufg.br']
##   Credits:      ['Copyright © 2025 LEEDMOL. All rights reserved.']
##   Date:         ['17.09.2025']
##   Version:      ['0.0.1']
##   Status:       ['Development']
##   Language:     ['Python']
##   Description:  ['Module to plot the results of the simulation']

import matplotlib.pyplot as plt
from pandas import read_csv

class Plotter():
    def __init__(self, name, target, polarAxis):
        if '.' in name:
            self.name = name.split('.')[0]
        else:
            self.name = name
        self.polarAxis = polarAxis

        if target == 'jgap':
            self.plot_jgap()
        elif target == 'polarizability':
            self.plot_polarizability()

    def plot_jgap(self):
        data = read_csv('OmegaGolden.csv')
        data = data.drop_duplicates(subset=['omega'])
        data = data.sort_values(by='omega')
        data.to_csv('OmegaGolden.csv', index=False)

        fig = plt.figure(figsize=(6,6))
        plt.plot(data['omega'], data['jgap'], marker='o', linestyle='-', color='b')
        plt.xlabel('$\\mathbf{\\omega}$ (bohr$\mathbf{^{-1}}$)', fontsize=14, fontweight='bold')
        plt.ylabel('$\\mathbf{J_{GAP}}$ (ev)', fontsize=14, fontweight='bold')
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.savefig('{}_JGAP.png'.format(self.name), dpi=300)

    def plot_polarizability(self):
        data = read_csv('OmegaGolden.csv')
        data = data.drop_duplicates(subset=['omega'])
        data = data.sort_values(by='omega')
        data.to_csv('OmegaGolden.csv', index=False)

        fig = plt.figure(figsize=(6,6))
        plt.plot(data['omega'], data['polarizability({})'.format(self.polarAxis)], marker='o', linestyle='-', color='b')
        plt.xlabel('$\\mathbf{\\omega}$ (bohr$\mathbf{^{-1}}$)', fontsize=14, fontweight='bold')
        plt.ylabel(fr'$\mathbf{{\alpha_{{{self.polarAxis}}}}}$ (a.u.)',fontsize=14, fontweight='bold')

        plt.grid(True, linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.savefig('{}_Polarizability.png'.format(self.name), dpi=300)