#!/usr/bin/env python3

"""
Module that makes an object that contains a list of all the contigs in the file

It takes the file_path as arg:

example:
    ReadMultifasta(<file_path>)

The object can than be used to get all the contigs in the file.

example:
    object.contigs # gives the contigs from the file

Examples
------------
'Examples/tester_1.fasta' as file and printing the contigs of the object:S
    ['ATGGCGTAA', 'ATGTAA']

with wrong file:
    /!\ NO FILE FOUND /!\
    The file can not be found.
    Check if the path is correct
    This error comes from readMultifasta.py
    Examples/tester.fasta is not an existing path

"""
# IMPORTS
import re
from DNA_seq import DNA_seq

# METADATA

__author__ = 'Rick Venema'
__status__ = 'In Development'
__version__ = '1.1'


class ReadMultifasta:
    """
    Class that accepts a file and than reads it to get the contigs in that file
    """

    def __init__(self, file_path):
        """
        :param:
            file_path
        """
        self.path = file_path  # the file path
        self.data = self.open_file()  # all the data in the file
        self.contigs = self.read_file()

    def open_file(self):
        """
        :return:
            file: the entire file in data

        :except:
            if file does not exist it will output an Error message.
        """
        try:
            file = open(self.path)
            return file

        except FileNotFoundError:
            print("/!\ NO FILE FOUND /!\ ")
            print("The file can not be found. \nCheck if the path is correct")
            print("This error comes from readMultifasta.py")
            print("{} is not an existing path".format(self.path))
            exit()

    def read_file(self):
        """
        :return:
            contigs: a list off all the contigs in the file.
        """
        contigs = []
        contig = ''
        for line in self.data:  # Iterates over all the data in the file
            if line.startswith('>'):  # If the line is a header
                if contig != '':  # If the contig is not empty append the contig
                    contigs.append(contig)
                contig = ''  # Empty contig
            else:
                contig += line.rstrip("\n")  # If the line is not a header, add the line to the contig
        contigs.append(contig)  # Append the last contig to contigs
        self.check_if_valid(contigs)
        if contigs:
            DNA_list = []
            for contig in contigs:
                tmp = DNA_seq(contig)
                DNA_list.append(tmp)
            return DNA_list
        else:
            print("/!\ There are no contigs in the file /!\ ")
            print("{} does not contain any contigs".format(self.path))

    @staticmethod
    def check_if_valid(contigs):
        """
        :param contigs:

        :return:if the contig is not valid. It will remove it from the list
        """
        for contig in contigs:
            m = re.fullmatch('[ATGC]*', contig)
            if not m:
                contigs.remove(contig)

if __name__ == '__main__':
    test = ReadMultifasta('Examples/subset1.fasta')
    for i, contig in enumerate(test.contigs):
        contig.make_fasta("Examples/test.fasta", "Test_Contig_" + str(i) + "_ORF", append=(i != 0))
