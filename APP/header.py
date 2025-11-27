##   PYTHON FILE HEADER #
##
##   File:         [header.py]
##
##   Author(s):    ['Pedro H.F Matias']
##   Site(s):      ['https://github.com/phfmatias']
##   Email(s):     ['phfmatias@discente.ufg.br']
##   Credits:      ['Copyright © 2025 LEEDMOL. All rights reserved.']
##   Date:         ['15.09.2025']
##   Version:      ['0.0.1']
##   Status:       ['Development']
##   Language:     ['Python']
##   Description:  ['Header file for the application']
##   Usage:		   ['from APP.header import *']

class header:
    def __init__(self):

        self.headerfile = open('OmegaGolden.out','w')
        self.csvfile = open('OmegaGolden.csv','w')

        headertxt='''                                                                                                                                                                          
######################################################################################################################################################
                                                                                                                                                      
    &&(                &%&&&&&&          &&&&&&&%        &&&&&&&%&&&&&&&%&   &&&                   &&&    &&&&&&%&&&&&&&%&&&&&&%   &&&               
    %&(              &&&               &%&               &&&             &&& &&&%&(              &&&%&| %&&&                  &&%& &%&               
    &&(              &&&               &%&               &&&             &&& &&& &&&&          &%&  &&| %&&&                  &&%& &&&               
    %&(              &%&%&%&%&%&%&%&%& &%&%&%&%&%&%&%&%& &%&             &%& &%&   &%&%      &%&    %&| %&%&                  %&%& &%&               
    &&(              &&&               &%&               &&&             &&& &&&     (&&% .&&&      &&% /&&&&&&&,,,,,,,,,,&&&&&&%  &&&               
     &&&%&&&%&&&%&&&% &&%&&&%&&&%&&&%&  %&&&%&&&%&&&%&&& &&&%&&&%&&&%&&&%&&  &&&        %&&&        %&%            /%&              %&&&%&&&%&&&%&&& 
     
######################################################################################################################################################

     Script for Functional Optmization via Golden Ratio by: Thiago O. Lopes , Mateus R. Barbosa, Pedro H.F. Matias and Heibbe C.B. Oliveira
                                                
######################################################################################################################################################
                                                                                                                                                                                         
'''
        self.headerfile.write(headertxt)

    