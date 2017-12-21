#!/usr/bin/env python3

import sys
import argparse


def filter_file(in_path, out_path, thresholds, filter_columns, check_with_or, larger_than):
    for i, filter_column in enumerate(filter_columns):
        filter_columns[i] = filter_column - 1
    to_output = True
    with open(in_path, "r") as in_file:
        with open(out_path, "w") as out_file:
            for line in in_file:
                splitline = line.split("\t")
                for i, column in enumerate(filter_columns):
                    if (not (float(splitline[column]) < thresholds[i]) and not larger_than) \
                            or (not (float(splitline[column]) > thresholds[i]) and larger_than):
                        to_output = False
                    elif check_with_or:
                        break
                if to_output:
                    out_file.write(line)
                to_output = True


def main():
    parser = argparse.ArgumentParser(
        description="Filters blast data based on specified columns"
                    " and/or a specified threshold for each column, and puts the result in a new file.")
    parser.add_argument('-I', type=str, metavar="input_file",
                        help="The tabular file to get blast data from.", required=True)
    parser.add_argument('-O', type=str, metavar="output_file",
                        help="The tabular file to output filtered data to.", required=True)
    parser.add_argument('-t', type=float, nargs="+", metavar="thresholds",
                        help="The threshold values to filter by.", required=True)
    parser.add_argument('-c', type=int, nargs="+", metavar="filter_columns",
                        help="The columns to filter on."
                             " Needs to be in the same order as the thresholds.", required=True)
    parser.add_argument('-o', help="If enabled, will check if at least one of the columns meets the threshold."
                                   "If false, all columns must meet the threshold.", action="store_true")
    parser.add_argument('-L', help="If enabled, will check if the value of the columns is larger than the threshold."
                                   "Defaults to false.", action="store_true")
    args = parser.parse_args()
    try:
        filter_file(args.I, args.O, args.t, args.c, args.o, args.L)
        print("Executed succesfully.")
    except FileNotFoundError:
        print("File not found, please check your path.")
    # except TypeError:
    #    print("Invalid type found in the specified column.")


if __name__ == "__main__":
    sys.exit(main())
