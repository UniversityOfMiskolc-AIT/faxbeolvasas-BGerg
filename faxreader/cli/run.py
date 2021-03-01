from faxreader.cli.cli_parser import parse
from faxreader.core.handle_data import *

def handle(args):



    a = read_lines_from_file("nu.txt")
    print(interpret_numbers_list_and_covert_to_str(a))




if __name__ == "__main__":
    handle(parse())
