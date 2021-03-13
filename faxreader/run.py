from faxreader.cli.cli_parser import parse
from faxreader.core.handle_data import *


def handle(args):
    lines = read_lines_from_file(args.input_file)
    number_of_accounts = get_number_of_accounts(lines)
    for account_index in range(number_of_accounts):
        account = []
        for number_index in range(1, 10):
            digit = get_digit(account_index, number_index, lines)
            account.append(digit)
        checked_account = check_account_number("".join(account))
        create_and_write_to_report_file(args.saveto,checked_account)


if __name__ == "__main__":
    handle(parse())
