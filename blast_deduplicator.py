#!/usr/bin/env python3

import sys
import argparse
import math
import re


def filter_file(in_path, out_path):
    maxvalue = 0
    previous_id = ""
    maxline = ""
    with open(in_path, "r") as in_file:
        with open(out_path, "w") as out_file:
            for line in in_file:
                splitline = line.split("\t")
                check_value = float(splitline[2]) - math.log(float(splitline[10]))
                if splitline[0] == previous_id:
                    if check_value > maxvalue:
                        maxvalue = check_value
                        maxline = line
                else:
                    maxvalue = check_value
                    if maxline:
                        maxline = maxline.split("\t")
                        bacterium = re.search(r"\[(.*?)\]", maxline[24])
                        bacterium_name = bacterium.group(0).strip("[]")
                        out_file.write(">{0}\n".format(bacterium_name.replace(" ", "_")))
                        out_file.write(maxline[20] + "\n")
                    maxline = line
                previous_id = splitline[0]


def main():
    parser = argparse.ArgumentParser(
        description="Filters blast data based on specified columns"
                    " and/or a specified threshold for each column, and puts the result in a new file.")
    parser.add_argument('-I', type=str, metavar="input_file",
                        help="The tabular file to get blast data from.", required=True)
    parser.add_argument('-O', type=str, metavar="output_file",
                        help="The tabular file to output filtered data to.", required=True)
    args = parser.parse_args()
    try:
        filter_file(args.I, args.O)
        print("Executed succesfully.")
    except FileNotFoundError:
        print("File not found, please check your path.")
    # except TypeError:
    #    print("Invalid type found in the specified column.")


if __name__ == "__main__":
    sys.exit(main())
