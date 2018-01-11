#!/usr/bin/env python3

import argparse
import sys
from readMultifasta import ReadMultifasta


def main():
    parser = argparse.ArgumentParser(
        description="Processes a fasta file to find orfs, and puts these orfs in a new fasta file.")
    parser.add_argument('-f', type=str, metavar="fasta_file",
                        help="The fasta file to extract data from.", required=True)
    parser.add_argument('-H', type=str, metavar="header",
                        help="The header to use for the output fasta file."
                             " This will get an incrementing number appended.", required=True)
    parser.add_argument('-o', type=str, metavar="output",
                        help="The output file.", required=True)
    args = parser.parse_args()
    fasta = ReadMultifasta(args.f)
    for i, contig in enumerate(fasta.contigs):
        contig.make_fasta(args.o, args.H + "_" + str(i) + "_ORF", append=(i != 0))


if __name__ == '__main__':
    sys.exit(main())
