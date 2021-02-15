import argparse


def parse():
    parser = argparse.ArgumentParser(description='Read paper documents'
                                                 ' and create a file with same content',
                                     epilog='Enjoy the digital world! :)')

    parser.add_argument(action='store',
                        type=str,
                        metavar='',
                        help='sets input file name')
    parser.add_argument('-s',
                        '--saveto',
                        action='store',
                        type=str,
                        default='accountNumbers.txt',
                        metavar='',
                        help='set output file name for account numbers')

    return parser.parse_args()
