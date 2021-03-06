#!/usr/bin/env python3

"""
This module creates DNA string objects from the input
It can be used to find the open reading frames within a DNA sequence
"""
import re

# METADATA VARIABLES
__author__ = "Wouter Schuiten and Hylke Middel"
__status__ = "Ready"
__version__ = "1.1"


class DNA_seq:

    def __init__(self, sequence):
        """
        sequence input is a DNA string
        class will determine open reading frames within DNA string
        """
        self._sequence = None
        self.sequence = sequence
        self.orfs = self.orf_finder()

    @property
    def sequence(self):
        """
        getter for sequence
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        """
        setter for sequence, checks if input is valid
        shuts down program on no valid input
        """
        try:
            if not re.match('^[ACTGactg]+$', sequence):
                print('Something went wrong, one of your input strings was not a valid DNA string (did not contain only A, C, T and G), program shut down')
                exit()
            self._sequence = sequence
        except TypeError as errort:
            print('Expected a string, but recieved different type. The following error occured: ', errort)
            exit()

    def orf_finder(self):
        """
        Takes a DNA string as input
        Returns the open reading frames (start till stopcodon, stopcodon included) from DNA string
        """
        orfs = []
        for item in re.findall(r'(?=(ATG(?:...)+?)(TAG|TGA|TAA))', self.sequence):
            orfs.append(item[0]+item[1])
        return orfs

    def make_fasta(self, path, identifier, use_orfs=True, append=False):
        """A function to make a fasta file. Takes the following arguments:

        :param path: The path to write the fasta file to.
         (WARNING: This will overwrite any existing files with the same path
         if append is not specified.)
        :param use_orfs: Make a fasta file with orfs?
         If not, make a fasta file with the stored sequence.
         Will make an empty file if there are no orfs.
        :param identifier: The identifier to use in the fasta header.
         There will be an "_n" appended with the orfs option enabled,
          where n increments with every sequence.
        :param append: Append to an existing fasta file?
        :return: Nothing
        """
        if append:
            mode = "a"
        else:
            mode = "w"
        with open(path, mode) as fasta_file:
            if use_orfs:
                if self.orfs:
                    number = 0
                    for orf in self.orfs:
                        fasta_file.write(">{0}_{1}\n".format(identifier, number))
                        fasta_file.write(orf + "\n")
                        number += 1
                else:
                    return
            else:
                fasta_file.write(">" + identifier + "\n")
                fasta_file.write(self.sequence)
