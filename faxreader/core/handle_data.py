from typing import List
from faxreader.core.number import SevenSegmentNumber


def get_digit(fax_row: int, fax_column: int, line: List[str]) -> str:
    """
    :param fax_column: Number of the column in fax file. (1 fax column = 3 ordinary columns)
    :param fax_row: Number of the line in fax file. (1 fax line = 3 ordinary lines)
    :param line: 1 line of the fax message
    :return: returns the number represented in the fax message
    """

    column_offset = fax_column * 3  # 1 fax line = 3 line in a file
    row_offset = fax_row * 4 # 1 row line

    top = line[0 + row_offset][column_offset - 3:column_offset]
    middle = line[1 + row_offset][column_offset - 3:column_offset]
    bottom = line[2 + row_offset][column_offset - 3:column_offset]

    number = top + middle + bottom

    _number_repository = {
        SevenSegmentNumber.zero: "0",
        SevenSegmentNumber.one: "1",
        SevenSegmentNumber.two: "2",
        SevenSegmentNumber.three: "3",
        SevenSegmentNumber.four: "4",
        SevenSegmentNumber.five: "5",
        SevenSegmentNumber.six: "6",
        SevenSegmentNumber.seven: "7",
        SevenSegmentNumber.eight: "8",
        SevenSegmentNumber.nine: "9",
    }

    try:
        return _number_repository[number]
    except KeyError:
        return "?"



def check_account_number(account_number: str)  -> str:
    """
    This validate correctness of account number.
    """
    checksum = 0
    if "?" in account_number:
        return account_number + " ILL"
    else:
        for i, j in zip(account_number, range(1, 10)):
            checksum += int(i) * j
        if (checksum % 11) != 0:
            return account_number + " ERR"
        else:
            return account_number


def read_lines_from_file(filename: str) -> List[str]:
    with open(filename) as f:
        return f.readlines()

def get_number_of_accounts(lines_in_file: list):
    """
    Four lines is equal one valid account number
    """
    return len(lines_in_file)//4

def create_and_write_to_report_file(output_file_name: str, account_number: str):
    with open(output_file_name, '+a') as f:
        f.write(account_number+"\n")
