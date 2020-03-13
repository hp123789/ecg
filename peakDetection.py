#!/usr/bin/env python3

import math
import sys
import argparse
import copy

from scipy import signal



def find_Peak(data):

    #print(data[2500][1])
    average = 0
    sum = 0

    test = []

    #print(range(len(data) - 1))

    for i in range(len(data)):
        #print(data[i][0])

        #print(data[i][0])

        test.append(data[i][0])

    for i in range(len(data)):
        #print(data[i][0])

        #print(i)

        print(test[i])

    #print(test)





def read_file(filename):

    file_reader = open(filename,'r')
    data = []

    for line in file_reader:
        number_strings = line.split()
        numbers = [float(n) for n in number_strings]
        data.append(numbers)

    #print(data[0][0])

    find_Peak(data)

    #contents = file_reader.read()
    #file_reader.close()

    #print(contents)


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('--file', type=str, help='file to be processed')

    args = parser.parse_args()

    print ('file: {}'.format(args.file))

    if not args.file:
        print("Need --file=<ics filename>")


    read_file(args.file)


if __name__ == "__main__":
    main()