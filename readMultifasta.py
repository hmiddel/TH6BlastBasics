"""
Module that makes an object that contains a list of all the contigs in the file

It takes the file_path as arg:

example:
    ReadMultifasta(<file_path>)

The object can than be used to get all the contigs in the file.

example:
    object.contigs # gives the contigs from the file

"""

# METADATA

__author__ = 'Rick Venema'
__status__ = 'In Development'
__version__ = '1.0'


class ReadMultifasta:
    """
    Class that accepts a file and than reads it to get the contigs in that file
    """

    def __init__(self, file_path):
        """
        :param:
            file_path
        """
        self.path = file_path
        self.data = self.open_file()
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
        for line in self.data:
            if line.startswith('>'):
                if contig != '':
                    contigs.append(contig)
                contig = ''
            else:
                contig += line.rstrip("\n")
        contigs.append(contig)
        return contigs


if __name__ == '__main__':
    test = ReadMultifasta('Examples/tester.fasta')
    print(test.contigs)
