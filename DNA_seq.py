#!/usr/bin/env python3

'''
This module creates DNA string objects from the input
It can be used to find the open reading frames within a DNA sequence
'''

# METADATA VARIABLES
__author__ = "Wouter Schuiten"
__status__ = "Ready"
__version__ = "1.1"

import re

class DNA_seq:

    def __init__(self, sequence):
        '''
        sequence input is a DNA string
        class will determine open reading frames within DNA string
        '''
        self._sequence = None
        self.sequence = sequence
        self.ORFs = self.ORFfinder(sequence)

    @property
    def sequence(self):
        '''
        getter for sequence
        '''
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        '''
        setter for sequence, checks if input is valid
        shuts down program on no valid input
        '''
        try:
            if not re.match('^[ACTGactg]+$', sequence):
                print('Something went wrong, one of your input strings was not a valid DNA string (did not contain only A, C, T and G), program shut down')
                exit()
            self._sequence = sequence
        except TypeError as errort:
            print('Expected a string, but recieved different type. The following error occured: ', errort)
            exit()
        
    @staticmethod
    def ORFfinder(sequence):
        '''
        Takes a DNA string as input
        Returns the open reading fromes (start till stopcodon, stopcodon not included) from DNA string
        '''
        orfs = []
        for item in re.findall(r'(?=(ATG(?:...)*?)(TAG|TGA|TAA))', sequence):
            orfs.append(item[0]+item[1])
        return orfs


#TESTING DATA:

'''
sequences = ['ATGCCATGCTAACCTAA']
for sequence in sequences:
    contig = DNA_seq(sequence)
    print(contig.ORFs)


sequences = ['ATGGATGAGTAG']
['ATGGATGAG']

sequences = ['ATGGATGAG']
None

sequences = ['ATGGATGAGTAG', 'ATGCCATGCTAACCTAA']
['ATGGATGAG']
['ATGCCATGC', 'ATGCTAACC']
This one is important because we have multiple ORFs on different frames
of the second string
program finds both reading frames on second string

sequences = ['ASDAGFDFS']
Something went wrong, one of your input strings was not a valid DNA 
string (did not contain only A, C, T and G), program shut down

sequences = [1, 'ACTG']
Expected a string, but recieved different type. The following error 
occured:  expected string or bytes-like object

sequences = []
***Nothing will happen***
'''
