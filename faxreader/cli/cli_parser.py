import argparse


def parse():
    parser = argparse.ArgumentParser(description='Read account numbers from paper documents'
                                                 ' and create a file with same content',
                                     epilog='Enjoy the digital world! :)')

    parser.add_argument('account_number')
    parser.add_argument('-s',
                        '--saveto',
                        action='store',
                        type=str,
                        default='accountNumbers.txt',
                        metavar='',
                        help='set output file name for account numbers')

    return parser.parse_args()
